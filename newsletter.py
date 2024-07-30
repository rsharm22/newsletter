# This script contain the class to generate the article content and send out the newsletter.
from datetime import date, timedelta
from credentials import right, left, center, national
import abstractivesummary
import emailhtml


class NewsLetter:
    def __init__(self, client, from_email, app_password):
        self.client = client
        self.from_email = from_email
        self.app_password = app_password

    @staticmethod
    def _get_top_articles(articles):
        top_articles = {}
        titles = set()
        i = 0
        attempts = 0

        while len(top_articles) < 5 and attempts < 1:
            try:
                title = articles['articles'][i]['title']
                desc = articles['articles'][i]['description']
                url = articles['articles'][i]['url']

                if title and title != '[Removed]' and desc and desc != '[Removed]' and url and url != '[Removed]' and not str(
                        desc).endswith('…') and title not in titles:
                    top_articles[i] = [title, desc, url]
                    titles.add(title)
            except (IndexError, KeyError):
                attempts += 1
                pass
            i += 1

        return top_articles

    def _create_and_send_email(self, to_email, top_articles, category):
        summary = abstractivesummary.generate_ai_summary(articles=top_articles)
        html = emailhtml.generate_email_v2(articles=top_articles, abstractive_summaries=summary, cat=category)
        emailhtml.send_email(from_email=self.from_email, email_pass=self.app_password, recipients=to_email,
                             content=html, cat=category)

    def get_global(self, to_email, language='en'):
        articles = self.client.get_top_headlines(language=language)
        top_articles = self._get_top_articles(articles)
        self._create_and_send_email(to_email, top_articles, 'Global')

    def get_national(self, to_email, language='en'):
        articles = self.client.get_top_headlines(language=language,
                                                 sources=national)
        top_articles = self._get_top_articles(articles)
        self._create_and_send_email(to_email, top_articles, 'National')

    def get_category(self, to_email, category_name):
        articles = self.client.get_top_headlines(category=category_name, language='en', country='us')
        top_articles = self._get_top_articles(articles)
        self._create_and_send_email(to_email, top_articles, category_name)

    def get_right(self, to_email):
        articles = self.client.get_top_headlines(sources=right, language='en')
        top_articles = self._get_top_articles(articles)
        self._create_and_send_email(to_email, top_articles, 'Right-Leaning')

    def get_left(self, to_email):
        articles = self.client.get_top_headlines(sources=left, language='en')
        top_articles = self._get_top_articles(articles)
        self._create_and_send_email(to_email, top_articles, 'Left-Leaning')

    def get_center(self, to_email):
        articles = self.client.get_top_headlines(sources=center, language='en')
        top_articles = self._get_top_articles(articles)
        self._create_and_send_email(to_email, top_articles, 'Center')

    def get_source(self, to_email, source_list):
        articles = self.client.get_top_headlines(sources=source_list, language='en')
        top_articles = self._get_top_articles(articles)
        self._create_and_send_email(to_email, top_articles, 'Source-Specified')

    def get_search(self, to_email, keyword, source_list = 'none'):
        to_date = date.today()
        from_date = to_date - timedelta(6)
        if source_list == 'none':
            articles = self.client.get_top_headlines(qintitle=keyword,
                                                     language='en',
                                                     sort_by='relevancy',
                                                     from_param=from_date,
                                                     to=to_date)
        else:
            articles = self.client.get_top_headlines(qintitle=keyword,
                                                     sources=source_list,
                                                     language='en',
                                                     sort_by='relevancy',
                                                     from_param=from_date,
                                                     to=to_date)
        top_articles = self._get_top_articles(articles)
        self._create_and_send_email(to_email, top_articles, 'Center')

