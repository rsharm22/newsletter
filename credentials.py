# This file contains the sender credentials, News API key, and email list.

import os

# Sender credentials
from_email=os.environ['NEWS_API_EMAIL']

app_password=os.environ['NEWS_API_PASSWORD']

# Recipient list
email_list=os.environ['EMAIL_LIST']

# News API Key
news_api_key=os.environ['NEWS_API_KEY']

# List of news sources
right = 'breitbart-news,fox-news,national-review,the-american-conservative,the-wall-street-journal,the-washington-times'
left = 'al-jazeera-english,business-insider,cbs-news,cnn,mashable,msnbc,nbc-news,new-york-magazine,' \
       'the-huffington-post,the-washington-post,vice-news,wired'
center = 'abc-news,ars-technica,associated-press,axios,bloomberg,fortune,google-news,newsweek,politico,' \
         'reddit-r-all,reuters,the-hill,time'
national = 'abc-news,axios,breitbart-news,cbs-news,fox-news,msnbc,national-review,nbc-news,new-york-magazine,' \
           'politico,the-american-conservative,the-hill,the-washington-post,the-washington-times,usa-today '



