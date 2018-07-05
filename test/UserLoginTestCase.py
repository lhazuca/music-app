import json
import unittest
import requests


class UserLogginTestCase(unittest.TestCase):

    def test_loggin_y_loggout_JoseYYY(self):
        jsonData = {'name': 'Jose',
                    'lastName': 'Perez',
                    'userName': 'JoseYYY',
                    'password': 'Clave1234._5'}
        requests.put('http://localhost:8080/apiv1/users', json=jsonData)

        jsonData = {'password': 'Clave1234._5'}
        logginUserReq = requests.post('http://localhost:8080/apiv1/login/JoseYYY', json=jsonData)


        self.assertEqual(logginUserReq.status_code, 200)
        self.assertEqual(logginUserReq.reason, 'OK')
        self.assertEqual(logginUserReq.text, 'User logged-in')

        jsonData = {'userName': 'JoseYYY'}
        loggoutUserReq= requests.post('http://localhost:8080/apiv1/logout', json=jsonData)
        self.assertEqual(loggoutUserReq.status_code, 200)
        self.assertEqual(loggoutUserReq.reason, 'OK')
        self.assertEqual(loggoutUserReq.text, 'User logged-out')

    def test_loggin_already_user_loggedin_JoseYYY(self):
        jsonData = {'name': 'Jose',
                    'lastName': 'Perez',
                    'userName': 'JoseYYY',
                    'password': 'Clave1234._5'}
        requests.put('http://localhost:8080/apiv1/users', json=jsonData)

        jsonData = {'password': 'Clave1234._5'}
        requests.post('http://localhost:8080/apiv1/login/JoseYYY', json=jsonData)

        jsonData = {'password': 'Clave1234._5'}
        logginUserReq = requests.post('http://localhost:8080/apiv1/login/JoseYYY', json=jsonData)

        self.assertEqual(logginUserReq.status_code, 400)
        self.assertEqual(logginUserReq.reason, 'Bad Request')
        self.assertEqual(logginUserReq.text, 'User not logged-in')

    def test_loggin_already_user_loggedout_JoseYYY(self):
        jsonData = {'name': 'Jose',
                    'lastName': 'Perez',
                    'userName': 'JoseYYY',
                    'password': 'Clave1234._5'}
        requests.put('http://localhost:8080/apiv1/users', json=jsonData)

        jsonData = {'userName': 'JoseYYY'}
        loggoutUserReq = requests.post('http://localhost:8080/apiv1/logout', json=jsonData)


        self.assertEqual(loggoutUserReq.status_code, 400)
        self.assertEqual(loggoutUserReq.reason, 'Bad Request')
        self.assertEqual(loggoutUserReq.text, 'User not logged-out')


    def tearDown(self):
        requests.delete('http://localhost:8080/apiv1/users/JoseYYY')

if __name__ == '__main__':
    unittest.main()