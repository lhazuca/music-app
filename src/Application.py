import tornado.web
from src.DatabaseConnector.DataBaseConnector import DatabaseConnector
from src.requestHandler.ArtistHandler import ArtistHandler
from src.requestHandler.RootHandler import RootHandler

class Application(tornado.web.Application):

    def __init__(self):
        handlers = [
        (r"/", RootHandler),
        (r"/apiv1/artist/(.*)", ArtistHandler),

        ]
        settings = dict(debug=True)
        tornado.web.Application.__init__(self, handlers, **settings)
        self.db = DatabaseConnector.instance()
