from flask import render_template
# from . import main
from .requests import get_sources,get_articles
from .models import Source,Article
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular news
    title = 'News Highlight'
    general_sources = get_sources('general')
    business_sources = get_sources('business')
    sports_sources = get_sources('sports')
    technology_sources = get_sources('technology')

    return render_template('index.html', title = title, general = general_sources, business = business_sources, sports = sports_sources, technology = technology_sources)

@app.route('/articles/<id>')
def articles(id):
    '''View a specific source page and its articles'''
    articles = get_articles(id)
    title = f'{id}'
    return render_template('articles.html',id = id, articles = articles)
