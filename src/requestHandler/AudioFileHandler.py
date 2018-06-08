import tornado.web


class AudioFileHandler(tornado.web.RequestHandler):

    def get(self, filename):
        statusCode = 400
        statusMessage = 'Bad request'
        try:
            statusCode = 200
            statusMessage = self.application.db.getAudioFile(filename)
        except Exception as e:
            raise (e)
            statusCode = 400
            statusMessage = "Audio file not added"
        self.set_status(statusCode)
        self.write(statusMessage)

    def post(self, filename):

        statusCode = 200
        statusMessage = 'Audio file added'
        try:
            filename = self.get_argument('filename')
            isAudioFile = bool(self.get_argument('isAudioFile'))
            self.application.db.addAudioFile(filename, isAudioFile)
        except Exception as e:
            raise e
            statusCode = 400
            statusMessage = "Audio file not added"
        self.set_status(statusCode)
        self.write(statusMessage)

    def delete(self, filename):
        statusCode = 200
        statusMessage = 'Audio File deleted'
        try:
            self.application.db.deleteAudioFile(filename)
        except Exception as e:
            raise e
            statusCode = 400
            statusMessage = "Audio File not deleted"
        self.set_status(statusCode)
        self.write(statusMessage)
