import unittest
import requests
import json
from collections import namedtuple

from src.appConfig import ENV


class AlbumTestCase(unittest.TestCase):


    def getFilePath(self,fileName):
        return 'rsc/'+fileName if ENV == 'dev' else 'test/rsc/'+fileName


    def test_addAlbum_AlbumX_to_user_JoseXXX(self):
        jsonData = {'name': 'Jose',
                    'lastName': 'Perez',
                    'userName': 'JoseYYY',
                    'password': 'Clave1234._5'}
        requests.put('http://localhost:8080/apiv1/users', json=jsonData)

        #Primero me logueo
        jsonData = {'password': 'Clave1234._5'}
        requests.post('http://localhost:8080/apiv1/login/JoseYYY', json=jsonData)

        albumJsonData = {'name': 'AlbumX',
                         'year': '2010',
                         'owner': 'JoseYYY'}
        addAlbumReq = requests.put('http://localhost:8080/apiv1/albums', json=albumJsonData)
        self.assertEqual(addAlbumReq.status_code, 200)
        self.assertEqual(addAlbumReq.reason, 'OK')
        self.assertEqual(addAlbumReq.text, 'Album added')

        #Me deslogueo
        jsonData = {'userName': 'JoseYYY'}
        requests.post('http://localhost:8080/apiv1/logout', json=jsonData)

    def test_get_Nonexistent_Album(self):
        data = {'albumLikeName':'albumNone'}
        getAlbumReq = requests.get('http://localhost:8080/apiv1/albums',data=data)
        self.assertEqual(getAlbumReq.status_code, 200)
        self.assertEqual(getAlbumReq.reason, 'OK')
        jsonResponse = json.loads(getAlbumReq.text)
        self.assertEqual(len(jsonResponse), 0)

    def test_updateAlbumXData(self):
        postData = {'name': 'Jose',
                    'lastName': 'Perez',
                    'userName': 'JoseYYY',
                    'password': 'Clave1234._5'}
        requests.put('http://localhost:8080/apiv1/users', json=postData)

        #Primero me logueo
        jsonData = {'password': 'Clave1234._5'}
        requests.post('http://localhost:8080/apiv1/login/JoseYYY', json=jsonData)

        albumJsonData = {'name': 'AlbumX',
                         'year': '2010',
                         'owner': 'JoseYYY'}
        requests.put('http://localhost:8080/apiv1/albums', json=albumJsonData)
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

        #Me deslogueo
        jsonData = {'userName': 'JoseYYY'}
        requests.post('http://localhost:8080/apiv1/logout', json=jsonData)

    def test_getAllAlbums(self):
        #Agrego dos albums a la BD
        postData = {'name': 'Jose',
                    'lastName': 'Perez',
                    'userName': 'JoseYYY',
                    'password': 'Clave1234._5'}
        requests.put('http://localhost:8080/apiv1/users', json=postData)
        # Primero me logueo
        jsonData = {'password': 'Clave1234._5'}
        requests.post('http://localhost:8080/apiv1/login/JoseYYY', json=jsonData)

        firstAlbumJsonData = {'name': 'AlbumX',
                         'year': '2010',
                         'owner': 'JoseYYY'}
        requests.put('http://localhost:8080/apiv1/albums', json=firstAlbumJsonData)
        secondAlbumJsonData = {'name': 'AlbumY',
                         'year': '2012',
                         'owner': 'JoseYYY'}
        requests.put('http://localhost:8080/apiv1/albums', json=secondAlbumJsonData)
        getAlbumReq = requests.get('http://localhost:8080/apiv1/albums')
        jsonResponse = json.loads(getAlbumReq.text)
        self.assertEqual(len(jsonResponse), 2)

        #Me deslogueo
        jsonData = {'userName': 'JoseYYY'}
        requests.post('http://localhost:8080/apiv1/logout', json=jsonData)


    def test_AddTrackToAnAlbum(self):
        #Agrego User
        userPostData = {'name': 'Jose',
                    'lastName': 'Perez',
                    'userName': 'JoseYYY',
                    'password': 'Clave1234._5'}
        requests.put('http://localhost:8080/apiv1/users', json=userPostData)
        #Agrego Album
        firstAlbumJsonData = {'name': 'AlbumX',
                         'year': '2010',
                         'owner': 'JoseYYY'}
        # Primero me logueo
        jsonData = {'password': 'Clave1234._5'}
        requests.post('http://localhost:8080/apiv1/login/JoseYYY', json=jsonData)

        requests.put('http://localhost:8080/apiv1/albums', json=firstAlbumJsonData)
        #Agrego Track
        fileFullPath = self.getFilePath('metallica_fuell.mp3')
        files= {'file': open(fileFullPath, 'rb')}
        putData = {'trackName': 'Tema 1', 'owner': 'JoseYYY'}
        addTrackReq = requests.post('http://localhost:8080/apiv1/tracks', files=files,data=putData)
        #Agrego Track a Album
        addTrackData = {'tracks' : [ 'Tema 1']}
        putTrackReq = requests.put('http://localhost:8080/apiv1/albums/AlbumX', json=addTrackData)
        self.assertEqual(200,putTrackReq.status_code)
        self.assertEqual('OK',putTrackReq.reason)
        self.assertEqual('Album updated', putTrackReq.text)

        #Me deslogueo
        jsonData = {'userName': 'JoseYYY'}
        requests.post('http://localhost:8080/apiv1/logout', json=jsonData)





    def tearDown(self):
        requests.delete('http://localhost:8080/apiv1/albums/AlbumX')
        requests.delete('http://localhost:8080/apiv1/albums/AlbumY')
        requests.delete('http://localhost:8080/apiv1/users/JoseYYY')
        requests.delete('http://localhost:8080/apiv1/tracks/Tema 1')



if __name__ == '__main__':
    unittest.main()
