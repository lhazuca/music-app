import json


def getAlbumLikeNameParser(albums):
    return json.dumps([{'albumName':album.name,'genre':album.genre} for album in albums])