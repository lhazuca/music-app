import tornado.web
import json


class PlaylistHandler(tornado.web.RequestHandler):

    def delete(self, playlistId):
        statusCode = 200
        statusMessage = 'Playlist deleted'
        try:
            self.application.db.deletePlaylist(playlistId)
        except Exception as e:
            raise e
            statusMessage = 'Playlist not deleted'
            statusCode = 400
        self.set_status(statusCode)
        self.write(statusMessage)





