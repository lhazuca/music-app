import json
from src.requestHandler.BaseHandler import BaseHandler

class AlbumHandler(BaseHandler):

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
            if(not data.__contains__('tracks')):
                self.editAlbumInfo(albumId, data)
            else:
                self.addTracks(albumId, data)

        except Exception as e:
            raise e
            statusMessage = 'Album not deleted'
            statusCode = 400
        self.set_status(statusCode)
        self.write(statusMessage)

    def editAlbumInfo(self, albumId, data):
        if self.isLoggendin(self.getOwner(albumId)):
            self.application.db.updateAlbum(albumId, data)

    def addTracks(self, albumId, data):
        if self.isLoggendin(self.getOwner(albumId)):
            tracks = data['tracks']
            self.application.db.addTracksToAlbum(albumId, tracks)

    def getOwner(self, albumId):
        return self.application.db.getAlbumOwner(albumId)