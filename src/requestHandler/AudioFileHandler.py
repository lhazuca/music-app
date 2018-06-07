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
            artist = self.get_argument('artist')
            self.application.db.addAudioFile(filename, artist)
        except Exception as e:
            raise e
            statusCode = 400
            statusMessage = "Audio file not added"
        self.set_status(statusCode)
        self.write(statusMessage)
