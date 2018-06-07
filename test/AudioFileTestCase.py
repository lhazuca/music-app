import unittest
import requests
import json

class AudioFileTestCase(unittest.TestCase):

    def test_addAudioFile_Music_MP3(self):

        postData = {'filename': 'Music MP3', 'artist': 'Jose'}
        addAudioFileReq = requests.post('http://localhost:8080/apiv1/audiofile/MusicMP3', data=postData)

        self.assertEqual(addAudioFileReq.status_code, 200)
        self.assertEqual(addAudioFileReq.reason, 'OK')
        self.assertEqual(addAudioFileReq.text, 'Audio file added')

        getAudioFileReq = requests.get('http://localhost:8080/apiv1/audiofile/MusicMP3')
        self.assertEqual(getAudioFileReq.status_code, 200)
        jsonResponse = json.loads(getAudioFileReq.text)
        self.assertEqual(jsonResponse['audiofile']['filename'], 'Music MP3')
        self.assertEqual(jsonResponse['artist']['artist'], 'Jose')


    # TODO: Agregar el delete
    # TODO: ver porque tira error 500

    # def tearDown(self):
    #
    #     requests.delete('http://localhost:8080/apiv1/audiofile/MusicMP3')



if __name__ == '__main__':
    unittest.main()
