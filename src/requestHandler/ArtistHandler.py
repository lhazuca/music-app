import tornado.web


class ArtistHandler(tornado.web.RequestHandler):


    def get(self,stageName):
        statusCode = 400
        statusMessage = 'Bad request'
        try:
            statusCode = 200
            statusMessage=self.application.db.getArtist(stageName)
        except Exception as e :
            raise (e)
            statusCode = 400
            statusMessage = "Artist not added"
        self.set_status(statusCode)
        self.write(statusMessage)


    def post(self, stageName):

        statusCode = 200
        statusMessage = 'Artist added'
        try:
            name = self.get_argument('name')
            lastName = self.get_argument('lastName')
            age = int(self.get_argument('age'))
            self.application.db.addArtist(stageName,name,lastName,age)
        except Exception as e:
            raise e
            statusCode = 400
            statusMessage = "Artist not added"
        self.set_status(statusCode)
        self.write(statusMessage)


    def delete(self,stageName):
        statusCode = 200
        statusMessage = 'Artist deleted'
        try:
            self.application.db.deleteArtist(stageName)
        except Exception as e:
            raise e
            statusCode = 400
            statusMessage = "Artist not deleted"
        self.set_status(statusCode)
        self.write(statusMessage)