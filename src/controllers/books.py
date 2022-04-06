import resource
from flask import Flask
from flask_restplus import Api, Resource

from src.server.instance import server

app, api = server.app, server.api

books_db = [
    {
        'id': 0, 'title': 'Art of War',
    },
    {
        'id': 1, 'title': 'Travels'
    }
]

@api.route('/books')
def method_name():
    pass
class BookList(Resource):
    def get(self):
        return books_db