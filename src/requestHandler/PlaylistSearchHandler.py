import tornado.web
import json

class PlaylistSearchHandler(tornado.web.RequestHandler):

    def put(self):
        statusCode = 200
        statusMessage = 'Playlist added'
        try:
            data = json.loads(self.request.body.decode('utf-8'))
            playlistName = data['playlistName']
            userName = data['userName']
            description = int(data['description'])
            self.application.db.addPlaylist(playlistName, userName, description)
        except Exception as e:
            raise e
            statusCode = 400
            statusMessage = "Playlist not added"
        self.set_status(statusCode)
        self.write(statusMessage)