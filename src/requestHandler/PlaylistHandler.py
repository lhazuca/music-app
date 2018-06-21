import tornado.web
import json


class PlaylistHandler(tornado.web.RequestHandler):

    def get(self, playlistId):
        statusCode = 200
        statusMessage = ''
        try:
            statusMessage = self.application.db.getPlaylist(playlistId)
        except Exception as e:
            raise e
            statusCode = 400
            statusMessage = "Bad request"
        self.set_status(statusCode)
        self.write(statusMessage)

    def put(self, playlistId):
        statusCode = 200
        statusMessage = 'Playlist updated'
        try:
            data = json.loads(self.request.body.decode('utf-8'))
            self.application.db.updatePlaylist(playlistId, data)
        except Exception as e:
            raise e
            statusMessage = 'Playlist not updated'
            statusCode = 400
        self.set_status(statusCode)
        self.write(statusMessage)

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





