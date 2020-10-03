import os

class Config:
    '''
    General configuration parent class
    '''
    BOOKS_API_KEY= os.environ.get('BOOKS_API_KEY')
    # BOOKS_CATEGORY_BASE_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    BOOKS_CATEGORY_BASE_URL = 'https://www.googleapis.com/books/v1/volumes?q={}&key={}'
    # ARTICLES_BASE_URL = 'https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}'
    SECRET_KEY = os.environ.get('SECRET_KEY')

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}