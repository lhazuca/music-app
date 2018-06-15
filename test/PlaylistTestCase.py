import json
import unittest
import requests


class PlaylistTestCase(unittest.TestCase):

    def test_addPlaylist_RockClassics_JoseYYY_OldRockClassics(self):
        jsonData = {'name': 'Jose',
                    'lastName': 'Perez',
                    'age': 34,
                    'userName': 'JoseYYY',
                    'password': 'Clave1234._5'}
        addUserReq = requests.post('http://localhost:8080/apiv1/user/create', json=jsonData)

        jsonDataSong1 = {'isAudioFile': True, 'filename': 'Rock baby'}
        jsonDataSong2 = {'isAudioFile': True, 'filename': 'All night'}
        addAudioFileReq1 = requests.post('http://localhost:8080/apiv1/audiofile/Rock baby', data=jsonDataSong1)
        addAudioFileReq2 = requests.post('http://localhost:8080/apiv1/audiofile/All night', data=jsonDataSong2)

        jsonDataPlaylist = {'playlistName': 'Rock Classics',
                    'userName': 'JoseYYY',
                    'description': 'Old rock classics',
                    'songs': ['Rock baby', 'All night']}
        addPlaylistReq = requests.post('http://localhost:8080/apiv1/playlist/create', json=jsonDataPlaylist)

        self.assertEqual(addPlaylistReq.status_code, 200)
        self.assertEqual(addPlaylistReq.reason, 'OK')
        self.assertEqual(addPlaylistReq.text, 'Playlist added')

    def test_get_Playlist(self):

        searchPlaylistLikeName = requests.get('http://localhost:8080/apiv1/playlist/get/Rock Classics')

        jsonResponse = json.loads(searchPlaylistLikeName.text)
        self.assertEqual(searchPlaylistLikeName.status_code, 200)
        self.assertEqual(searchPlaylistLikeName.reason, 'OK')
        self.assertEqual(len(jsonResponse), 1)
        res = [];
        for playlist in jsonResponse:
            res.append(playlist['playlistName'])
        self.assertTrue(res.__contains__('Rock Classics'))
        self.delete();

    def delete(self):
        requests.delete('http://localhost:8080/apiv1/user/rm/JoseYYY')
        deletePlaylist = requests.delete('http://localhost:8080/apiv1/playlist/rm/Rock Classics')
        requests.delete('http://localhost:8080/apiv1/audiofile/Rock baby')
        requests.delete('http://localhost:8080/apiv1/audiofile/All night')


if __name__ == '__main__':
    unittest.main()