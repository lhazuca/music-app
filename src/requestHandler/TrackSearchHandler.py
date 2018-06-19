import json

import tornado.web

class TrackSearchHandler(tornado.web.RequestHandler) :

    def get(self):
        statusCode = 200
        statusMessage = ''
        try:
            trackLikeName = self.get_argument('trackLikeName')
            statusMessage = self.application.db.getTrackLikeName(trackLikeName)
        except Exception as e:
            raise e
            statusCode = 400
            statusMessage = "Bad request"
        self.set_status(statusCode)
        self.write(statusMessage)

    def post(self):
        statusCode = 200
        statusMessage = 'Track added'
        try :
            data = json.loads(self.request.body.decode('utf-8'))
            trackName = data['trackName']
            owner = data['owner']
            fileContent =data['fileContent']
            self.application.db.addTrack(owner,trackName,fileContent)
        except Exception as e:
            raise e
            statusCode = 400
            statusMessage = "Track not added"
        self.set_status(statusCode)
        self.write(statusMessage)