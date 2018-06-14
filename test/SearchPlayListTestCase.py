import unittest
import requests
import json


class PlaylistTestCase(unittest.TestCase):

    def test_search_Playlist_that_contains_a_string(self):
        jsonDataUser = {'name': 'Jose',
                        'lastName': 'Perez',
                        'age': 34,
                        'userName': 'JoseYYY',
                        'password': 'Clave1234._5'}
        addUserReq = requests.post('http://localhost:8080/apiv1/user', json=jsonDataUser)

        jsonDataSong1 = {'isAudioFile': True, 'filename': 'Rock baby'}
        jsonDataSong2 = {'isAudioFile': True, 'filename': 'All night'}
        jsonDataSong3 = {'isAudioFile': True, 'filename': 'La complicidad'}
        jsonDataSong4 = {' isAudioFile': True, 'filename': 'Cada quien'}

        addAudioFileReq1 = requests.post('http://localhost:8080/apiv1/audiofile/Rock baby', data=jsonDataSong1)
        addAudioFileReq2 = requests.post('http://localhost:8080/apiv1/audiofile/All night', data=jsonDataSong2)
        addAudioFileReq3 = requests.post('http://localhost:8080/apiv1/audiofile/La complicidad', data=jsonDataSong3)
        addAudioFileReq4 = requests.post('http://localhost:8080/apiv1/audiofile/Cada quien', data=jsonDataSong4)

        jsonDataPlaylist = {'playlistName': 'Rock Classics',
                            'userName': 'JoseYYY',
                            'description': 'Old rock classics',
                            'songs': ['Rock baby', 'All night']}
        addPlaylistReq = requests.post('http://localhost:8080/apiv1/playlist', json=jsonDataPlaylist)

        jsonDataPlaylist2 = {'playlistName': 'Reggae',
                            'userName': 'JoseYYY',
                            'description': 'Reggae',
                            'songs': ['La complicidad', 'Cada quien']}
        addPlaylistReq2 = requests.post('http://localhost:8080/apiv1/playlist', json=jsonDataPlaylist2)

        getData = {'playlistName': 'Rock'}
        searchPlaylistLikeName = requests.get('http://localhost:8080/apiv1/playlists', params=getData)

        jsonResponse = json.loads(searchPlaylistLikeName.text)
        self.assertEqual(searchPlaylistLikeName.status_code, 200)
        self.assertEqual(searchPlaylistLikeName.reason, 'OK')
        self.assertEqual(len(jsonResponse), 1)
        res = [];
        for playlist in jsonResponse:
            res.append(playlist['playlistName'])
        self.assertTrue(res.__contains__('Rock Classics'))
        self.assertFalse(res.__contains__('Reggae'))

    def tearDown(self):
        jsonDataPlaylist = {'playlistName': 'Rock Classics'}
        requests.delete('http://localhost:8080/apiv1/playlist', json=jsonDataPlaylist)
        jsonDataPlaylist2 = {'playlistName': 'Reggae'}
        requests.delete('http://localhost:8080/apiv1/playlist', json=jsonDataPlaylist2)

        jsonDataUser = {'userName': 'JoseYYY'}
        requests.delete('http://localhost:8080/apiv1/user', json=jsonDataUser)

        requests.delete('http://localhost:8080/apiv1/audiofile/Rock baby')
        requests.delete('http://localhost:8080/apiv1/audiofile/All night')
        requests.delete('http://localhost:8080/apiv1/audiofile/La complicidad')
        requests.delete('http://localhost:8080/apiv1/audiofile/Cada quien')

