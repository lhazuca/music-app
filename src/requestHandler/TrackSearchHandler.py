import json
import tornado.web
from src.appConfig import ENV


class TrackSearchHandler(tornado.web.RequestHandler):



    def get(self):
        statusCode = 200
        statusMessage = ''
        try:
            trackLikeName = self.get_argument('trackLikeName')
            statusMessage = self.application.db.getTrackLikeName(trackLikeName)
        except tornado.web.MissingArgumentError as e:
            statusMessage = self.application.db.getAllTracks()
        except Exception as e :
            raise e
            statusCode=400
            statusMessage= 'Bad request'
        self.set_status(statusCode)
        self.write(statusMessage)


    def post(self):
        statusCode = 200
        statusMessage = 'Track added'

        try:
            fileInfo = self.request.files['file'][0]
            fileName = fileInfo['filename']
            owner = self.get_argument('owner')
            trackName = self.get_argument('trackName')
            fh = open(self.getFilePath(fileName), 'wb')
            fh.write(fileInfo['body'])
            fh.close()
            fileContent = fileName
            self.application.db.addTrack(owner,trackName,fileContent)
        except Exception as e:
            raise e
            statusCode = 400
            statusMessage = "Track not added"
        self.set_status(statusCode)
        self.write(statusMessage)

    def getFilePath(self,fileName):
        return 'mp3Files/'+fileName if ENV == 'dev' else 'src/mp3Files/'+fileName