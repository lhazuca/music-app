import unittest
import requests


class UserTestCase(unittest.TestCase):

    def test_addUser_JoseYYY_Jose_Perez_34(self):

        jsonData = {'name': 'Jose',
                    'lastName': 'Perez',
                    'userName':'JoseYYY',
                    'password': 'Clave1234._5'}
        addUserReq = requests.put('http://localhost:8080/apiv1/user', json=jsonData)

        self.assertEqual(addUserReq.status_code, 200)
        self.assertEqual(addUserReq.reason, 'OK')
        self.assertEqual(addUserReq.text, 'User Created')

    def tearDown(self):
        requests.delete('http://localhost:8080/apiv1/user/JoseYYY')
