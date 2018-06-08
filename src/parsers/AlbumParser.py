import json


def getAlbumLikeNameParser(albums):
    return json.dumps([{'albumName':album.name,'albumYear':album.albumYear} for album in albums])