import tornado.web

from src.DatabaseConnector.DataBaseConnector import DatabaseConnector
from src.requestHandler.AlbumHandler import AlbumHandler
from src.requestHandler.ArtistHandler import ArtistHandler
from src.requestHandler.TrackHandler import TrackHandler
from src.requestHandler.PlaylistHandler import PlaylistHandler
from src.requestHandler.RootHandler import RootHandler
from src.requestHandler.TrackSearchHandler import TrackSearchHandler
from src.requestHandler.UserHandler import UserHandler


class Application(tornado.web.Application):

    def __init__(self):
        settings = dict(debug=True)
        handlers = [
            (r"/", RootHandler),
            (r"/apiv1/artist/(.*)", ArtistHandler),
            (r"/apiv1/playlist/create", PlaylistHandler),
            (r"/apiv1/playlist/get/(.*)", PlaylistHandler),
            (r"/apiv1/playlist/rm/(.*)", PlaylistHandler),
            (r"/apiv1/track/(.*)", TrackHandler),
            (r"/apiv1/track", TrackSearchHandler)
        ]
        tornado.web.Application.__init__(self, handlers, **settings)
        self.db = DatabaseConnector.instance()
