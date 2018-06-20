import tornado.web
from src.validationFunctions import validPassword
from hashlib import sha512
import json


class UserSearchHandler(tornado.web.RequestHandler):

    # create
    def put(self):
        statusCode = 200
        statusMessage = 'User Created'
        try:
            data = json.loads(self.request.body.decode('utf-8'))
            userName = data['userName']
            name = data['name']
            lastName = data['lastName']
            password = data['password']

            if validPassword(password):
                cryptPass = sha512(password.encode('utf-8')).hexdigest()
                self.application.db.addUser(userName, cryptPass, name, lastName)
            else:
                statusCode = 400
                statusMessage = "Bad request"
        except Exception as e:
            raise e
            statusCode = 400
            statusMessage = "User was not created"
        self.set_status(statusCode)
        self.write(statusMessage)

