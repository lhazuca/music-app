import json


def getTrackParser(track):
    return json.dumps({'track': {'trackName': track.trackName,
                                     'fileContent': track.fileContent}})


def getTrackLikeNameParser(tracks):
    return json.dumps([{'trackName': track.trackName, 'fileContent': track.fileContent}
                       for track in tracks])
