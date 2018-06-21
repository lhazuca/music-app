import json
import unittest
import requests


class PlaylistTestCase(unittest.TestCase):

    def test_addPlaylist_RockClassics_JoseYYY_OldRockClassics(self):

        jsonDataUser = {'name': 'Jose',
                    'lastName': 'Perez',
                    'age': 34,
                    'userName':'JoseYYY',
                    'password': 'Clave1234._5'}
        addUserReq = requests.put('http://localhost:8080/apiv1/users', json=jsonDataUser)

        self.assertEqual(addUserReq.status_code, 200)
        self.assertEqual(addUserReq.reason, 'OK')
        self.assertEqual(addUserReq.text, 'User Created')

        jsonDataSong1 = {'trackName': 'Rock baby', 'fileContent': 'contenido', 'owner': 'JoseYYY'}
        jsonDataSong2 = {'trackName': 'All night', 'fileContent': 'contenido', 'owner': 'JoseYYY'}
        addAudioFileReq1 = requests.put('http://localhost:8080/apiv1/tracks', json=jsonDataSong1)
        addAudioFileReq2 = requests.put('http://localhost:8080/apiv1/tracks', json=jsonDataSong2)

        self.assertEqual(addAudioFileReq1.status_code, 200)
        self.assertEqual(addAudioFileReq1.reason, 'OK')
        self.assertEqual(addAudioFileReq1.text, 'Track added')

        self.assertEqual(addAudioFileReq2.status_code, 200)
        self.assertEqual(addAudioFileReq2.reason, 'OK')
        self.assertEqual(addAudioFileReq2.text, 'Track added')

        jsonDataPlaylist = {'playlistName': 'Rock Classics',
                    'userName': 'JoseYYY',
                    'description': 'Old rock classics',
                    'songs': ['Rock baby', 'All night']}
        addPlaylistReq = requests.post('http://localhost:8080/apiv1/playlist', json=jsonDataPlaylist)

        self.assertEqual(addPlaylistReq.status_code, 200)
        self.assertEqual(addPlaylistReq.reason, 'OK')
        self.assertEqual(addPlaylistReq.text, 'Playlist added')

    def tearDown(self):
        jsonDataPlaylist = {'playlistName': 'Rock Classics'}
        requests.delete('http://localhost:8080/apiv1/playlist', json=jsonDataPlaylist)

        requests.delete('http://localhost:8080/apiv1/users/JoseYYY')

        requests.delete('http://localhost:8080/apiv1/tracks/Rock baby')
        requests.delete('http://localhost:8080/apiv1/tracks/All night')