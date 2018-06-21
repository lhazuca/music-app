import unittest
import requests
import json


class PlaylistTestCase(unittest.TestCase):

    def test_addPlaylist_RockClassics_to_user_Max01(self):
        postData = {'name': 'Max', 'lastName': 'Johnson', 'age': 27}
        requests.post('http://localhost:8080/apiv1/artist/Max01', data=postData)
        playlistJsonData = {'playlistName': 'RockClassics',
                         'userName': 'Max01',
                         'description': 'Good old rock classics'}
        addPlaylistReq = requests.put('http://localhost:8080/apiv1/playlist', json=playlistJsonData)
        self.assertEqual(addPlaylistReq.status_code, 200)
        self.assertEqual(addPlaylistReq.reason, 'OK')
        self.assertEqual(addPlaylistReq.text, 'Playlist added')

    def test_get_Nonexistent_Playlist(self):
        getData = {'playlistLikeName': 'something'}
        getPlaylistReq = requests.get('http://localhost:8080/apiv1/playlist', data=getData)
        self.assertEqual(getPlaylistReq.status_code, 200)
        self.assertEqual(getPlaylistReq.reason, 'OK')
        jsonResponse = json.loads(getPlaylistReq.text)
        self.assertEqual(len(jsonResponse), 0)

    def tearDown(self):
        jsonData = {'playlistName': 'RockClassics'}
        requests.delete('http://localhost:8080/apiv1/artist/Max01')
        requests.delete('http://localhost:8080/apiv1/playlist/RockClassics')

