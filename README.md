# newsletter
Creating a newsletter where subscribers can curate their content to their interests. Options include creating a custom newsletter based on keywords/interests and news sources, or selecting from various prebuilt newsletters. Each newsletter email includes article titles, link to each of the articles, as well as an AI generated summary of each article.

***Some of the code has been modified to protect any personal information.***

File Details:
  1. abstractivesummary.py - functions to generate an AI summary of each article
  2. credentials.py - contains the secret News API key and email sender credentials
  3. email.py - functions to generate the email body for the newsletter
  4. newsletter.py - defines the NewsLetter class used to pull article details based on user preferences and send out the newsletter
  5. send.py - contains the function to select the correct newsletter format based on user input
  6. sqs.py - pulls in user data from AWS SQS and sends out email

**Status:** This is an ongoing project, and I am currently working to create a front-end. All functionality is working.
