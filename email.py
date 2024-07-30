# This script contains the 'generate_email' function which creates the HTML email body based on the type of search
# requested, and the 'send_email' function to send the content to users.

from credentials import categories
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime


def generate_email_v2(articles, abstractive_summaries, cat=categories):
    indices = list(articles.keys())[:5]  # Limit to 5 articles
    if isinstance(cat, str):
        title = 'Trending ' + cat + ' News'
    else:
        title = 'Trending News Summary'

    # HTML email content with inline CSS for styling
    email_content = f"""
    <html>
        <head>
            <style>
                body {{ font-family: Arial, sans-serif; }}
                .article {{ margin-bottom: 18px; padding-bottom: 12px; border-bottom: 1px solid #ccc; }}
                .title {{ font-size: 18px; font-weight: bold; color: #333; }}
                .summary-label {{ font-size: 14px; font-weight: bold; color: #666; }}
                .description {{ font-size: 14px; color: #333; }}
                .url {{ font-size: 12px; color: #007bff; }}
            </style>
        </head>
        <body>
            <h2 style="color: #007bff;">{title}</h2>
    """

    for count, i in enumerate(indices):
        email_content += f"""
        <div class="article">
            <div class="title">{count + 1}. {articles[i][0]}</div>
            <div class="summary">
                <span class="summary-label">AI Generated Summary:</span> 
                <span class="description">{abstractive_summaries[i]}</span>
            </div>
            <div class="url"><a href="{articles[i][2]}" style="text-decoration: none; color: #007bff;">Read More</a></div>
        </div>
        """

    email_content += """
        </body>
    </html>
    """

    return email_content


def send_email(from_email, email_pass, recipients, content, cat=categories):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, email_pass)

    if isinstance(cat, str):
        subject = str(datetime.today().strftime('%m/%d')) + ' AI Newsletter: ' + cat
    else:
        subject = str(datetime.today().strftime('%m/%d')) + ' AI Newsletter'

    for recip in recipients:
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = recip
        msg['Subject'] = subject
        msg.attach(MIMEText(content, 'html'))
        server.sendmail(from_email, recip, msg.as_string())

    server.quit()
