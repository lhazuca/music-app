import json
import unittest
from collections import namedtuple

import requests


class UserTestCase(unittest.TestCase):

    def test_addUser_JoseYYY_Jose_Perez_34(self):
        jsonData = {'name': 'Jose',
                    'lastName': 'Perez',
                    'userName': 'JoseYYY',
                    'password': 'Clave1234._5'}
        addUserReq = requests.put('http://localhost:8080/apiv1/users', json=jsonData)

        self.assertEqual(addUserReq.status_code, 200)
        self.assertEqual(addUserReq.reason, 'OK')
        self.assertEqual(addUserReq.text, 'User Created')

    def test_getUserByUserName(self):
        jsonData = {'name': 'Jose',
                    'lastName': 'Perez',
                    'userName': 'JoseYYY',
                    'password': 'Clave1234._5'}
        requests.put('http://localhost:8080/apiv1/users', json=jsonData)

        getUserReq = requests.get('http://localhost:8080/apiv1/users/JoseYYY')

        self.assertEqual(getUserReq.status_code, 200)
        self.assertEqual(getUserReq.reason, 'OK')
        userResponse = json.loads(getUserReq.text, object_hook=lambda d: namedtuple('User', d.keys())(*d.values()))
        self.assertTrue('Jose', userResponse.user.name)



    def test_getNonExistentUserByUserName(self):
        getUserReq = requests.get('http://localhost:8080/apiv1/users/JoseYYY')

        self.assertEqual(getUserReq.status_code, 200)
        self.assertEqual(getUserReq.reason, 'OK')
        self.assertEqual(getUserReq.text, 'Username not found')

    def test_updateAUserUserName(self):
        jsonData = {'name': 'Jose',
                    'lastName': 'Perez',
                    'userName': 'JoseYYY',
                    'password': 'Clave1234._5'}
        requests.put('http://localhost:8080/apiv1/users', json=jsonData)

        jsonUpdate = {'name': 'Pepe'}
        updateUserReq = requests.put('http://localhost:8080/apiv1/users/JoseYYY',json=jsonUpdate)

        self.assertEqual(updateUserReq.status_code, 200)
        self.assertEqual(updateUserReq.reason, 'OK')

        getUserReq = requests.get('http://localhost:8080/apiv1/users/JoseYYY')
        updateResponse = json.loads(getUserReq.text, object_hook=lambda d: namedtuple('User', d.keys())(*d.values()))
        self.assertEqual('Pepe', updateResponse.user.name)

    def test_updateAUserPassword(self):
        jsonData = {'name': 'Jose',
                    'lastName': 'Perez',
                    'userName': 'JoseYYY',
                    'password': 'Clave1234._5'}
        requests.put('http://localhost:8080/apiv1/users', json=jsonData)

        jsonUpdate = {'password': 'ClaveNueva123'}
        updateUserReq = requests.put('http://localhost:8080/apiv1/login/JoseYYY',json=jsonUpdate)

        self.assertEqual(updateUserReq.status_code, 200)
        self.assertEqual(updateUserReq.reason, 'OK')

        getUserReq = requests.get('http://localhost:8080/apiv1/login/JoseYYY')
        updateResponse = json.loads(getUserReq.text, object_hook=lambda d: namedtuple('UserLogin', d.keys())(*d.values()))
        self.assertEqual('ClaveNueva123', updateResponse.userLogin.password)

    def tearDown(self):
        requests.delete('http://localhost:8080/apiv1/users/JoseYYY')