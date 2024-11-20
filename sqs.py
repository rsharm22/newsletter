# This file contains the code to run through the SQS AWS data and send emails to users

import boto3
import json
import logging
import article_details
from newsapi import NewsApiClient
from credentials import news_api_key
import send

logging.basicConfig(filename="pythonlogs.log", level=logging.INFO)

# connect to SQS
sqs = boto3.client('sqs', region_name='us-east-1')

# url of the SQS queue in aws
queue_url = 'https://sqs.us-east-1.amazonaws.com/767398019349/testQueue'

while True:
    print('monitoring queue')
    logging.info('monitoring queue')
    sqs_receive_response = sqs.receive_message(
        QueueUrl=queue_url,
        AttributeNames=[
            'SentTimestamp'
        ],
        MaxNumberOfMessages=1,
        MessageAttributeNames=[
            'All'
        ],
        WaitTimeSeconds=5
    )

    if 'Messages' in sqs_receive_response.keys():
        print('messages found in queue')
        logging.info('messages found in queue')
        messagesFound = True
    else:
        print('no messages found in queue')
        logging.info('no messages found in queue')
        messagesFound = False

    if (messagesFound):
        sqs_messages = sqs_receive_response['Messages']
        for message in sqs_messages:
            message_body = message['Body']
            receipt_handle = message['ReceiptHandle']

        inputs_for_news_api = json.loads(message_body)
        print('inputs from sqs: ')
        print(inputs_for_news_api)
        logging.info('inputs from sqs:')
        logging.info(inputs_for_news_api)

        # call the news api with the inputs that we have stored in inputs_for_news_api
        first_name = inputs_for_news_api['firstName']
        last_name = inputs_for_news_api['lastName']
        option = inputs_for_news_api['option']
        email_list = inputs_for_news_api['email_list']
        sources = inputs_for_news_api['sources']
        keywords = inputs_for_news_api['keywords']
        scheduleid = inputs_for_news_api['scheduleid']

        input_first_name = first_name.split()
        input_last_name = last_name.split()
        input_email = email_list.split()

        input_sources = ['cnn']
        input_option = option.split()
        keywords = keywords.split("_split_")
        input_keyword = keywords[0].split()

        if (input_keyword == []):
            input_keyword = ['none']
        input_additional = ['none']
        input_sources = sources.split("_split_")
        if (input_sources == ['']):
            input_sources = ['none']

        schedule_input = scheduleid

        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

        if (schedule_input == 'daily'):
            input_frequency = ['d']
        elif (schedule_input == 'unsubscribed'):
            input_frequency = ['none']
        elif (schedule_input in days):
            input_frequency = ['w']
        else:
            input_frequency = ['m']

        print("input option: ", input_option)
        print("keyword: ", input_keyword)
        print("second keyword: ", input_additional)
        print("sources: ", input_sources)

        newsAPIResponse = send.callNewsApi(input_option, input_keyword, input_additional, input_sources,
                                                  input_email)

        print(newsAPIResponse)

        if (newsAPIResponse == 'ok'):
            messageProcessed = True
            print('News API returned ok - message processed succesfully')
            logging.info('News API returned ok - message processed succesfully')
        else:
            messageProcessed = False
            print('News API did not return ok - message processed failed. Actually returned: ', newsAPIResponse)
            logging.info('News API did not return ok - message processed failed. Actually returned: ', newsAPIResponse)

        if (messageProcessed):
            sqs_delete_response = sqs.delete_message(
                QueueUrl=queue_url,
                ReceiptHandle=receipt_handle
            )
            delete_status_code = sqs_delete_response['ResponseMetadata']['HTTPStatusCode']
            if (delete_status_code == 200):
                print('message deleted succesfully')
                logging.info('message deleted succesfully')
            else:
                print('delete failed with status code: ', delete_status_code)
                logging.info('delete failed with status code: ', delete_status_code)
