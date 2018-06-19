import unittest
import requests
import json
from collections import namedtuple

class AlbumTestCase(unittest.TestCase):
    def test_addAlbum_AlbumX_to_user_JoseXXX(self):
        postData = {'name': 'Jose', 'lastName': 'Perez', 'age': 34}
        requests.post('http://localhost:8080/apiv1/artist/JoseYYY', data=postData)
        albumJsonData = {'name': 'AlbumX',
                         'year': '2010',
                         'owner': 'JoseYYY'}
        addAlbumReq = requests.put('http://localhost:8080/apiv1/album', json=albumJsonData)
        self.assertEqual(addAlbumReq.status_code, 200)
        self.assertEqual(addAlbumReq.reason, 'OK')
        self.assertEqual(addAlbumReq.text, 'Album added')

    def test_get_Nonexistent_Album(self):
        data = {'albumLikeName':'albumNone'}
        getAlbumReq = requests.get('http://localhost:8080/apiv1/album',data=data)
        self.assertEqual(getAlbumReq.status_code, 200)
        self.assertEqual(getAlbumReq.reason, 'OK')
        jsonResponse = json.loads(getAlbumReq.text)
        self.assertEqual(len(jsonResponse), 0)

    def test_updateAlbumXData(self):
        postData = {'name': 'Jose', 'lastName': 'Perez', 'age': 34}
        requests.post('http://localhost:8080/apiv1/artist/JoseYYY', data=postData)
        albumJsonData = {'name': 'AlbumX',
                         'year': '2010',
                         'owner': 'JoseYYY'}
        requests.put('http://localhost:8080/apiv1/album', json=albumJsonData)
        getAlbumReq = requests.get('http://localhost:8080/apiv1/album/AlbumX')
        albumResponse = json.loads(getAlbumReq.text, object_hook=lambda d: namedtuple('Album', d.keys())(*d.values()))
        self.assertEqual('AlbumX', albumResponse.album.albumName)
        self.assertEqual(2010, albumResponse.album.albumYear)
        putJsonData = {'albumYear' : 2000}
        requests.put('http://localhost:8080/apiv1/album/AlbumX', json=putJsonData)
        secondGetAlbumReq = requests.get('http://localhost:8080/apiv1/album/AlbumX')
        secondAlbumResponse = json.loads(secondGetAlbumReq.text, object_hook=lambda d: namedtuple('Album', d.keys())(*d.values()))
        self.assertEqual('AlbumX',secondAlbumResponse.album.albumName)
        self.assertEqual(2000,secondAlbumResponse.album.albumYear)



    def tearDown(self):
        jsonData = {'albumName': 'AlbumX'}
        requests.delete('http://localhost:8080/apiv1/artist/JoseYYY')
        requests.delete('http://localhost:8080/apiv1/album/AlbumX')



if __name__ == '__main__':
    unittest.main()
