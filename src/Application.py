import tornado.web

from src.DatabaseConnector.DataBaseConnector import DatabaseConnector
from src.requestHandler.AlbumSearchHandler import AlbumSearchHandler
from src.requestHandler.AlbumHandler import AlbumHandler
from src.requestHandler.TrackHandler import TrackHandler
from src.requestHandler.TrackSearchHandler import TrackSearchHandler
from src.requestHandler.RootHandler import RootHandler
from src.requestHandler.PlaylistHandler import PlaylistHandler
from src.requestHandler.PlaylistSearchHandler import PlaylistSearchHandler
from src.requestHandler.UserHandler import UserHandler
from src.requestHandler.UserSearchHandler import UserSearchHandler
from src.requestHandler.UserLoginHandler import UserLoginHandler
from src.requestHandler.UserLogoutHandler import UserLogoutHandler


class Application(tornado.web.Application):

    def __init__(self):
        settings = dict(debug=True)
        handlers = [
        (r"/", RootHandler),
        (r"/apiv1/playlists", PlaylistSearchHandler),
        (r"/apiv1/playlists/(.*)", PlaylistHandler),
        (r"/apiv1/users/(.*)", UserHandler),
        (r"/apiv1/login/(.*)", UserLoginHandler),
        (r"/apiv1/logout", UserLogoutHandler),
        (r"/apiv1/users", UserSearchHandler),
        (r"/apiv1/tracks/(.*)", TrackHandler),
        (r"/apiv1/tracks", TrackSearchHandler),
        (r"/apiv1/albums/(.*)", AlbumHandler),
        (r"/apiv1/albums", AlbumSearchHandler)
        ]
        tornado.web.Application.__init__(self, handlers, **settings)
        self.db = DatabaseConnector.instance()

