import urllib.request,json
from .models import Source,Article

# Getting api key
api_key = None
# Getting the news base url
source_base_url = None
articles_base_url = None

def configure_request(app):
    global api_key,source_base_url,articles_base_url
    api_key = app.config['NEWS_API_KEY']
    source_base_url = app.config['NEWS_SOURCES_BASE_URL']
    articles_base_url = app.config['NEWS_ARTICLES_API_BASE_URL']

def get_sources(category):
    '''Function that gets json response to our url request'''
    get_sources_url = source_base_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)

    return source_results

def process_results(source_list):
    '''
    Function that processes the source result and transform to a list of objects

    Args:
        source_list: A list of dictionaries that contain news sources

    Returns:
        source_results: A list of source objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')

        source_object = Source(id,name,description)
        source_results.append(source_object)

    return source_results



#....