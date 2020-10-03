from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_sources
from ..models import Category


# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    
    programming_books = get_sources('programming')
    # education_books = get_sources['categories']
    # business_books = get_sources('business')
    # romantic_books = get_sources('romantic')

   
    title = "Books"

    return render_template('index.html', title=title, programming_books=programming_books )
   



# @main.route('/sources/<id>')
# def articles(id):

#     '''
#     View root page function that returns the articles page and its data
#     '''
    
#     articles =get_articles(id)
#     title = f'{id}'

#     return render_template('articles.html', articles=articles, title=title)
