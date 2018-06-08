import json


def getAudioFileParser(audiofile):
    return json.dumps({'audiofile': {'filename': audiofile.filename,
                                     'isAudioFile': audiofile.isAudioFile}})
