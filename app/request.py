import urllib.request
import json
from .models import Category


# Getting api key
api_key = None

# Getting the book categories base url
category_base_url = None

# # Getting the news articles base url
# articles_base_url = None


def configure_request(app):
    global api_key, category_base_url
    api_key = app.config['BOOKS_API_KEY']
    category_base_url = app.config['BOOKS_CATEGORY_BASE_URL']
    # articles_base_url = app.config['ARTICLES_BASE_URL']


def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = category_base_url.format(category, api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)
        sources_results = None

        if get_sources_response['items']:
            sources_results_list = get_sources_response['items']
            sources_results = process_sources(sources_results_list)
    return sources_results


def process_sources(sources_list):
    '''
     Function that processes the news sources results and turns them into a list of objects

     Args:
             sources_list: A list of dictionaries that contain sources details

     Returns:
             sources_results: A list of sources objects
     '''
    sources_results = []
    print(sources_list)

    for source_item in sources_list:
        title = source_item['volumeInfo'].get('title')
        authors = source_item['volumeInfo'].get('authors')
        description = source_item['volumeInfo'].get('description')
        publisher = source_item['volumeInfo'].get('publisher')
        published_at = source_item['volumeInfo'].get('publishedDate')
        thumbnail = source_item['volumeInfo']['imageLinks'].get('thumbnail')
        

        sources_object = Category(title, authors, description, publisher, published_at, thumbnail)
        sources_results.append(sources_object)

    return sources_results

