import unittest
import requests


class PlaylistTestCase(unittest.TestCase):

    def test_addPlaylist_RockClassics_JoseYYY_OldRockClassics(self):

        jsonDataUser = {'name': 'Jose',
                    'lastName': 'Perez',
                    'age': 34,
                    'userName':'JoseYYY',
                    'password': 'Clave1234._5'}
        addUserReq = requests.post('http://localhost:8080/apiv1/user', json=jsonDataUser)

        self.assertEqual(addUserReq.status_code, 200)
        self.assertEqual(addUserReq.reason, 'OK')
        self.assertEqual(addUserReq.text, 'User Created')

        jsonDataPlaylist = {'playlistName': 'Rock Classics',
                    'userName': 'JoseYYY',
                    'description': 'Old rock classics'}
        addPlaylistReq = requests.post('http://localhost:8080/apiv1/playlist', json=jsonDataPlaylist)

        self.assertEqual(addPlaylistReq.status_code, 200)
        self.assertEqual(addPlaylistReq.reason, 'OK')
        self.assertEqual(addPlaylistReq.text, 'Playlist added')

    def tearDown(self):
        jsonDataPlaylist = {'playlistName': 'Rock Classics'}
        requests.delete('http://localhost:8080/apiv1/playlist', json=jsonDataPlaylist)

        jsonDataUser = {'userName':'JoseYYY'}
        requests.delete('http://localhost:8080/apiv1/user',json=jsonDataUser)
