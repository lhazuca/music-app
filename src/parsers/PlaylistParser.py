import json


def getPlaylistLikeNameParser(playlists):
    return json.dumps([{'playlistName': playlist.playlistName,
                        'description': playlist.description}
                       for playlist in playlists])

def getPlaylistParser(playlist):
    return json.dumps({'playlist': {'playlistName': playlist.playlistName, 'description': playlist.description}})