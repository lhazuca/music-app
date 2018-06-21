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
<<<<<<< HEAD
        addUserReq = requests.post('http://localhost:8080/apiv1/user/create', json=jsonData)
=======
        addUserReq = requests.put('http://localhost:8080/apiv1/users', json=jsonData)
>>>>>>> 9dbedda398da051ce095d329f1e2bafb6e573d32

        self.assertEqual(addUserReq.status_code, 200)
        self.assertEqual(addUserReq.reason, 'OK')
        self.assertEqual(addUserReq.text, 'User Created')

<<<<<<< HEAD
    def test_get_user(self):
        jsonData = {'name': 'Jose',
                    'lastName': 'Perez',
                    'age': 34,
                    'userName': 'JoseYYY',
                    'password': 'Clave1234._5'}
        addUserReq = requests.post('http://localhost:8080/apiv1/user/create', json=jsonData)

        getUserReq = requests.get('http://localhost:8080/apiv1/user/get/JoseYYY')
        self.assertEqual(getUserReq.status_code, 200)
        jsonResponse = json.loads(getUserReq.text)
        self.assertEqual(jsonResponse['users']['name'], 'Jose')
        self.assertEqual(jsonResponse['users']['lastName'], 'Perez')
        self.assertEqual(jsonResponse['users']['age'], 34)

    def test_edit_users(self):
        jsonData = {'name': 'Jose',
                    'lastName': 'Perez',
                    'age': 34,
                    'userName': 'JoseYYY',
                    'password': 'Clave1234._5'}
        addUserReq = requests.post('http://localhost:8080/apiv1/user/create', json=jsonData)

        jsonData = {"name":'Juance'}
        editUserReq = requests.put('http://localhost:8080/apiv1/user/edit/JoseYYY',jsonData)

        self.assertEqual(editUserReq .status_code, 200)
        self.assertEqual(editUserReq .reason, 'OK')
        self.assertEqual(editUserReq .text, 'Update user')

        getUserReq = requests.get('http://localhost:8080/apiv1/user/get/JoseYYY')
        self.assertEqual(getUserReq.status_code, 200)
        jsonResponse = json.loads(getUserReq.text)
        self.assertEqual(jsonResponse['users']['name'], 'Juance')

    def tearDown(self):
        deleteUser = requests.delete('http://localhost:8080/apiv1/user/rm/JoseYYY')

        self.assertEqual(deleteUser.status_code, 200)
        self.assertEqual(deleteUser.text, 'User deleted')
=======
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

    def test_updateAUserNameAndPassword(self):
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

    def tearDown(self):
        requests.delete('http://localhost:8080/apiv1/users/JoseYYY')
>>>>>>> 9dbedda398da051ce095d329f1e2bafb6e573d32
