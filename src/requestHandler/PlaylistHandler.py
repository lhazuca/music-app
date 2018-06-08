import tornado.web


class PlaylistHandler(tornado.web.RequestHandler):

    def get(self, playlistName):
        statusCode = 400
        statusMessage = 'Bad request'
        try:
            statusCode = 200
            statusMessage = self.application.db.getPlaylist(playlistName)
        except Exception as e:
            raise (e)
            statusCode = 400
            statusMessage = "Playlist not added"
        self.set_status(statusCode)
        self.write(statusMessage)

    def post(self, playlistName):

        statusCode = 200
        statusMessage = 'Playlist added'
        try:
            # playlistName = self.get_argument('playlistName')
            userName = self.get_argument('userName')
            description = self.get_argument('description')
            self.application.db.addPlaylist(playlistName, userName, description)
        except Exception as e:
            raise e
            statusCode = 400
            statusMessage = "Playlist not added"
        self.set_status(statusCode)
        self.write(statusMessage)

    def delete(self, playlistName):
        statusCode = 200
        statusMessage = 'Playlist deleted'
        try:
            self.application.db.deletePlaylist(playlistName)
        except Exception as e:
            raise e
            statusCode = 400
            statusMessage = "Playlist not deleted"
        self.set_status(statusCode)
        self.write(statusMessage)

