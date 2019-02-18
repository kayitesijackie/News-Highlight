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

#....