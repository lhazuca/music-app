import tornado.web
import json

class PlaylistSearchHandler(tornado.web.RequestHandler):

    def get(self):
        statusCode = 200
        statusMessage = ''
        try:
            playlistLikeName = self.get_argument('playlistLikeName')
            statusMessage = self.application.db.getPlaylistLikeName(playlistLikeName)
        except Exception as e:
            raise e
            statusCode = 400
            statusMessage = "Bad request"
        self.set_status(statusCode)
        self.write(statusMessage)

    def put(self):
        statusCode = 200
        statusMessage = 'Playlist added'
        try:
            data = json.loads(self.request.body.decode('utf-8'))
            playlistName = data['playlistName']
            userName = data['userName']
            description = data['description']
            self.application.db.addPlaylist(playlistName, userName, description)
        except Exception as e:
            raise e
            statusCode = 400
            statusMessage = "Playlist not added"
        self.set_status(statusCode)
        self.write(statusMessage)

    def delete(self):
        statusCode = 200
        statusMessage = 'Tracks deleted from playlist'
        try:
            data = json.loads(self.request.body.decode('utf-8'))
            playlistName = data['playlistName']
            tracks = data['tracks']
            self.application.db.deleteTracksFromPlaylist(playlistName, tracks)
        except Exception as e:
            raise e
            statusCode = 400
            statusMessage = "Tracks not deleted"
        self.set_status(statusCode)
        self.write(statusMessage)