import article_details
from newsapi import NewsApiClient
from credentials import news_api_key

# Initiating the news API
news = NewsApiClient(api_key=news_api_key)

def callNewsApi(input_option, input_keyword, input_additional, input_sources, email):

    if random_option == ['cus']:
        if random_keyword == ['none']:
            if random_sources == ['none']:
                response = letter.get_global(to_email=email)
            elif random_sources != ['none']:
                response = letter.get_source(to_email=email, source_list=random_sources)
        else:
            response = letter.get_search(to_email=email, keyword=random_keyword, source_list=random_sources)
    elif random_option == ['g'] or random_option == ['none']:
        response = letter.get_global(to_email=email)
    elif random_option == ['n']:
        response = letter.get_national(to_email=email)
    elif random_option == ['b']:
        response = letter.get_category(to_email=email, category_name='business')
    elif random_option == ['h']:
        response = letter.get_category(to_email=email, category_name='health')
    elif random_option == ['e']:
        response = letter.get_category(to_email=email, category_name='entertainment')
    elif random_option == ['sc']:
        response = letter.get_category(to_email=email, category_name='science')
    elif random_option == ['sp']:
        response = letter.get_category(to_email=email, category_name='sports')
    elif random_option == ['r']:
        response = letter.get_right(to_email=email)
    elif random_option == ['l']:
        response = letter.get_left(to_email=email)
    elif random_option == ['c']:
        response = letter.get_center(to_email=email)
        
return response
