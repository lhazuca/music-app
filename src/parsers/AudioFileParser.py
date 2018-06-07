import json


def getAudioFileParser(audiofile):
    return json.dumps({'audiofile': {'filename': audiofile.filename,
                                     'artist': audiofile.artist,
                                     'uploaded': audiofile.uploaded}})
