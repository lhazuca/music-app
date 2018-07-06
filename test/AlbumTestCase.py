import unittest
import json

from src.TestService import *
from collections import namedtuple

from src.appConfig import ENV


class AlbumTestCase(unittest.TestCase):


    def getFilePath(self,fileName):
        return 'rsc/'+fileName if ENV == 'dev' else 'test/rsc/'+fileName


    def test_addAlbum_AlbumX_to_user_JoseXXX(self):
        createJosePerez()

        logJosePerez()

        addAlbumReq = createAlbumXToJose()
        self.assertEqual(addAlbumReq.status_code, 200)
        self.assertEqual(addAlbumReq.reason, 'OK')
        self.assertEqual(addAlbumReq.text, 'Album added')

        logoutJosePerez()


    def test_get_Nonexistent_Album(self):
        data = {'albumLikeName':'albumNone'}
        getAlbumReq = requests.get('http://localhost:8080/apiv1/albums',data=data)
        self.assertEqual(getAlbumReq.status_code, 200)
        self.assertEqual(getAlbumReq.reason, 'OK')
        jsonResponse = json.loads(getAlbumReq.text)
        self.assertEqual(len(jsonResponse), 0)

    def test_updateAlbumXData(self):
        createJosePerez()

        logJosePerez()

        createAlbumXToJose()
        getAlbumReq = requests.get('http://localhost:8080/apiv1/albums/AlbumX')
        albumResponse = json.loads(getAlbumReq.text, object_hook=lambda d: namedtuple('Album', d.keys())(*d.values()))
        self.assertEqual('AlbumX', albumResponse.album.albumName)
        self.assertEqual(2010, albumResponse.album.albumYear)
        putJsonData = {'albumYear' : 2000}
        requests.put('http://localhost:8080/apiv1/albums/AlbumX', json=putJsonData)
        secondGetAlbumReq = requests.get('http://localhost:8080/apiv1/albums/AlbumX')
        secondAlbumResponse = json.loads(secondGetAlbumReq.text, object_hook=lambda d: namedtuple('Album', d.keys())(*d.values()))
        self.assertEqual('AlbumX',secondAlbumResponse.album.albumName)
        self.assertEqual(2000,secondAlbumResponse.album.albumYear)

        logoutJosePerez()

    def test_getAllAlbums(self):
        createJosePerez()
        logJosePerez()

        createAlbumXToJose()
        createAlbumYToJose()
        getAlbumReq = requests.get('http://localhost:8080/apiv1/albums')
        jsonResponse = json.loads(getAlbumReq.text)
        self.assertEqual(len(jsonResponse), 2)

        logoutJosePerez()


    def test_AddTrackToAnAlbum(self):
        createJosePerez()
        logJosePerez()

        createAlbumXToJose()
        self.createTrack()
        addTrackData = {'tracks' : [ 'Tema 1']}
        putTrackReq = requests.put('http://localhost:8080/apiv1/albums/AlbumX', json=addTrackData)
        self.assertEqual(200,putTrackReq.status_code)
        self.assertEqual('OK',putTrackReq.reason)
        self.assertEqual('Album updated', putTrackReq.text)

        logoutJosePerez()

    def createTrack(self):
        fileFullPath = self.getFilePath('metallica_fuell.mp3')
        files = {'file': open(fileFullPath, 'rb')}
        putData = {'trackName': 'Tema 1', 'owner': 'JoseYYY'}
        addTrackReq = requests.post('http://localhost:8080/apiv1/tracks', files=files, data=putData)

    def tearDown(self):
        requests.delete('http://localhost:8080/apiv1/albums/AlbumX')
        requests.delete('http://localhost:8080/apiv1/albums/AlbumY')
        requests.delete('http://localhost:8080/apiv1/users/JoseYYY')
        requests.delete('http://localhost:8080/apiv1/tracks/Tema 1')



if __name__ == '__main__':
    unittest.main()
