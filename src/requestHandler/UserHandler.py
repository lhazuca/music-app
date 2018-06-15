import json
from _sha512 import sha512

import tornado.web

from src.validationFunctions import validPassword


class UserHandler(tornado.web.RequestHandler):

    def get(self, userName):
        statusCode = 400
        statusMessage = 'Bad request'
        try:
            statusCode = 200
            statusMessage = self.application.db.getUser(userName)
        except Exception as e:
            raise e
            statusCode = 400
            statusMessage = "User not added"
        self.set_status(statusCode)
        self.write(statusMessage)

    def delete(self, stageName):
        statusCode = 200
        statusMessage = 'User deleted'
        try:
            self.application.db.deleteUser(stageName)
        except Exception as e:
            raise e
            statusCode = 400
            statusMessage = "User not deleted"
        self.set_status(statusCode)
        self.write(statusMessage)

    def post(self):
        statusCode = 200
        statusMessage = 'User Created'
        try:
            data = json.loads(self.request.body.decode('utf-8'))
            userName = data['userName']
            name = data['name']
            lastName = data['lastName']
            age = int(data['age'])
            password = data['password']

            if validPassword(password):
                cryptPass = sha512(password.encode('utf-8')).hexdigest()
                self.application.db.addUser(userName, cryptPass, name, lastName, age)
            else:
                statusCode = 400
                statusMessage = "Bad request"
        except Exception as e:
            statusCode = 400
            statusMessage = "Artist not added"
        self.set_status(statusCode)
        self.write(statusMessage)

    def put(self, *args, **kwargs):
        print(*args)
        statusCode = 200
        statusMessage = 'Update user'
        try:
            new_values = dict()
            name = self.get_argument('name', None)
            age = self.get_argument('age', None)
            userName = self.get_argument('userName', None)
            lastName = self.get_argument('lastName',None)
            if name:
                new_values['name'] = name
            if age:
                new_values['age'] = age
            if lastName:
                new_values['lastName'] = lastName
            if userName:
                new_values['userName'] = userName
                print(new_values)
            self.application.db.updateUser(*args, new_values)
        except Exception as e :
            raise(e)
            statusCode = 400
            statusMessage = 'Not update user. Error params'
        self.set_status(statusCode)
        self.write(statusMessage)

