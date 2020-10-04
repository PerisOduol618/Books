from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_sources
from ..models import Category
from flask_login import login_required


@main.route('/')
@login_required
def home():

    return render_template('home.html')

@main.route('/books')
@login_required
def index():

    '''
    View root page function that returns the index page and its data
    '''
    
    programming_books = get_sources('programming')
  

   
    title = "Books"

    return render_template('index.html', title=title, programming_books=programming_books )
   



