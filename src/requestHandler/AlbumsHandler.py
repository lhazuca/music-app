import tornado.web
import json


class AlbumsHandler(tornado.web.RequestHandler):


    def get(self):
        statusCode = 200
        statusMessage = ''
        try:
            albumLikeName = self.get_argument('albumLikeName')
            statusMessage=self.application.db.getAlbumLikeName(albumLikeName)
        except Exception as e:
            statusCode = 400
            statusMessage = "Bad request"
        self.set_status(statusCode)
        self.write(statusMessage)
