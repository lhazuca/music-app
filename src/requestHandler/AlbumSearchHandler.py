import json

import tornado.web

class AlbumSearchHandler(tornado.web.RequestHandler) :

    def get(self):
        statusCode = 200
        statusMessage = ''
        try:
            albumLikeName = self.get_argument('albumLikeName')
            statusMessage = self.application.db.getAlbumLikeName(albumLikeName)
        except Exception as e:
            raise e
            statusCode = 400
            statusMessage = "Bad request"
        self.set_status(statusCode)
        self.write(statusMessage)

    def post(self):
        statusCode = 200
        statusMessage = 'Album added'
        try :
            data = json.loads(self.request.body.decode('utf-8'))
            name = data['name']
            year = int(data['year'])
            owner = data['owner']
            self.application.db.addAlbum(name,year,owner)
        except Exception as e:
            raise e
            statusCode = 400
            statusMessage = "Album not added"
        self.set_status(statusCode)
        self.write(statusMessage)
