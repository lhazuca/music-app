import unittest
import requests
import json


class AlbumTestCase(unittest.TestCase):
    def test_addAlbum_AlbumX_to_user_JoseXXX(self):
        postData = {'name': 'Jose', 'lastName': 'Perez', 'age': 34}
        requests.post('http://localhost:8080/apiv1/artist/JoseYYY', data=postData)
        albumJsonData = {'name': 'AlbumX',
                         'year': '2010',
                         'owner': 'JoseYYY'}
        addAlbumReq = requests.post('http://localhost:8080/apiv1/album', json=albumJsonData)
        self.assertEqual(addAlbumReq.status_code, 200)
        self.assertEqual(addAlbumReq.reason, 'OK')
        self.assertEqual(addAlbumReq.text, 'Album added')

    def tearDown(self):
        requests.delete('http://localhost:8080/apiv1/artist/JoseYYY')


if __name__ == '__main__':
    unittest.main()
