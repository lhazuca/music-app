import json
import unittest

import requests


class AudioFileTestCase(unittest.TestCase):

    def test_addAudioFile_Music_MP3(self):
        postData = {'isAudioFile': True, 'filename': 'MusicMP3'}
        addAudioFileReq = requests.post('http://localhost:8080/apiv1/audiofile/MusicMP3', data=postData)

        self.assertEqual(addAudioFileReq.status_code, 200)
        self.assertEqual(addAudioFileReq.reason, 'OK')
        self.assertEqual(addAudioFileReq.text, 'Audio file added')

    def test_Search_Audiofile(self):
        postData1 = {'isAudioFile': True, 'filename': 'Music1'}
        addAudioFileReq1 = requests.post('http://localhost:8080/apiv1/audiofile/Music1', data=postData1)

        postData2 = {'isAudioFile': True, 'filename': 'Music2'}
        addAudioFileReq2 = requests.post('http://localhost:8080/apiv1/audiofile/Music2', data=postData2)

        postData3 = {'isAudioFile': True, 'filename': 'Cancion3'}
        addAudioFileReq3 = requests.post('http://localhost:8080/apiv1/audiofile/Cancion3', data=postData3)

        getData = {'filename': 'mu'}
        searchAudioFileLikeName = requests.get('http://localhost:8080/apiv1/audiofile.search', params=getData)
        jsonResponse = json.loads(searchAudioFileLikeName.text)
        self.assertEqual(searchAudioFileLikeName.status_code, 200)
        self.assertEqual(searchAudioFileLikeName.reason, 'OK')
        self.assertEqual(len(jsonResponse),2)
        res = []
        for audiofile in  jsonResponse:
            res.append(audiofile['filename'])
        self.assertTrue(res.__contains__('Music1'))
        self.assertTrue(res.__contains__('Music2'))
        self.assertFalse(res.__contains__('Cancion1'))

    def tearDown(self):
        requests.delete('http://localhost:8080/apiv1/audiofile/MusicMP3')
        requests.delete('http://localhost:8080/apiv1/audiofile/Music1')
        requests.delete('http://localhost:8080/apiv1/audiofile/Music2')
        requests.delete('http://localhost:8080/apiv1/audiofile/Cancion3')

if __name__ == '__main__':
    unittest.main()
