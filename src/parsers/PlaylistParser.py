import json


def getPlaylistParser(playlist):
    return json.dumps({'playlist': {'playlistName': playlist.playlistName,
                                    'userName': playlist.userName, 'description': playlist.description}})


def getPlaylistWithSubString(playlists):
    return json.dumps([{'playlistName': playlist.playlistName,
                        'userName': playlist.userName,
                        'description': playlist.description}
                       for playlist in playlists])
