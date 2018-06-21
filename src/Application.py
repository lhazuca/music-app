import tornado.web

from src.DatabaseConnector.DataBaseConnector import DatabaseConnector
from src.requestHandler.AlbumSearchHandler import AlbumSearchHandler
from src.requestHandler.AlbumHandler import AlbumHandler
from src.requestHandler.AudioFileHandler import AudioFileHandler
from src.requestHandler.PlaylistHandler import PlaylistHandler
from src.requestHandler.RootHandler import RootHandler
from src.requestHandler.UserHandler import UserHandler
from src.requestHandler.UserSearchHandler import UserSearchHandler


class Application(tornado.web.Application):

    def __init__(self):
        handlers = [
        (r"/", RootHandler),
        (r"/apiv1/users/(.*)", UserHandler),
        (r"/apiv1/users", UserSearchHandler),
        (r"/apiv1/playlist", PlaylistHandler),
        (r"/apiv1/audiofile/(.*)", AudioFileHandler),
        (r"/apiv1/albums/(.*)", AlbumHandler),
        (r"/apiv1/albums", AlbumSearchHandler)

        ]
        settings = dict(debug=True)
        tornado.web.Application.__init__(self, handlers, **settings)
        self.db = DatabaseConnector.instance()
