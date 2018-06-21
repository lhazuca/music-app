import tornado.web

from src.DatabaseConnector.DataBaseConnector import DatabaseConnector
from src.requestHandler.AlbumSearchHandler import AlbumSearchHandler
from src.requestHandler.AlbumHandler import AlbumHandler
from src.requestHandler.TrackHandler import TrackHandler
from src.requestHandler.PlaylistHandler import PlaylistHandler
from src.requestHandler.TrackSearchHandler import TrackSearchHandler
from src.requestHandler.PlaylistHandler import PlaylistHandler
from src.requestHandler.RootHandler import RootHandler
from src.requestHandler.UserHandler import UserHandler
from src.requestHandler.UserSearchHandler import UserSearchHandler


class Application(tornado.web.Application):

    def __init__(self):
        settings = dict(debug=True)
        handlers = [
        (r"/", RootHandler),
        (r"/apiv1/users/(.*)", UserHandler),
        (r"/apiv1/users", UserSearchHandler),
        (r"/apiv1/playlist", PlaylistHandler),
        (r"/apiv1/track/(.*)", TrackHandler),
        (r"/apiv1/track", TrackSearchHandler),
        (r"/apiv1/albums/(.*)", AlbumHandler),
        (r"/apiv1/albums", AlbumSearchHandler)
        ]
        tornado.web.Application.__init__(self, handlers, **settings)
        self.db = DatabaseConnector.instance()
