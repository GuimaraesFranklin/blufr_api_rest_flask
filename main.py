from xmlrpc.client import Server
from src.server.instance import server

from src.controllers.books import *

server.run()