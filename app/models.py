from . import db 

class Category:
    '''
    Sources class to define Sources Objects
    '''

    def __init__(self, title, authors, descripion, publisher, published_at, thumbnail):
        self.title = title
        self.authors = authors
        self.description = descripion
        self.publisher = publisher
        self.published_at = published_at
        self.thumbnail = thumbnail




class   