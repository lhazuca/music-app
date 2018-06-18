import json

import tornado.web

class AlbumHandler(tornado.web.RequestHandler) :

    def get(self,albumId):
        statusCode = 200
        statusMessage = ''
        try:
            statusMessage = self.application.db.getAlbum(albumId)
        except Exception as e:
            raise e
            statusCode = 400
            statusMessage = "Bad request"
        self.set_status(statusCode)
        self.write(statusMessage)

    def delete(self,albumId):
        statusCode = 200
        statusMessage = 'Album deleted'
        try:
            self.application.db.deleteAlbum(albumId)
        except Exception as e:
            raise e
            statusMessage = 'Album not deleted'
            statusCode = 400
        self.set_status(statusCode)
        self.write(statusMessage)

    def put(self,albumId):
        statusCode = 200
        statusMessage = 'Album updated'
        try:
            data=json.loads(self.request.body.decode('utf-8'))
            self.application.db.updateAlbum(albumId,data)
        except Exception as e:
            raise e
            statusMessage = 'Album not deleted'
            statusCode = 400
        self.set_status(statusCode)
        self.write(statusMessage)