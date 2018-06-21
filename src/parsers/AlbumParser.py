import json


def getAlbumLikeNameParser(albums):
    return json.dumps([{'albumName': album.albumName,'albumYear': album.albumYear} for album in albums])

def getAlbumParser(album):
    return  json.dumps({'album' : {'albumName' : album.albumName,
                                   'albumYear' : album.albumYear }})
