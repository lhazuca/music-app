import json
import tornado.web

class UserLoginHandler(tornado.web.RequestHandler):

    # update password
    def put(self, userName):
        statusCode = 200
        statusMessage = 'User Password Updated'
        try:
            password = json.loads(self.request.body.decode('utf-8'))
            self.application.db.updateUserCredentials(userName, password)
        except Exception as e:
            raise e
            statusCode = 400
            statusMessage = "User Password was not updated"
        self.set_status(statusCode)
        self.write(statusMessage)

    #Testing password get
    def get(self, userName):
        statusCode = 200
        statusMessage = 'User Login Obtained'
        try:
            statusMessage = self.application.db.getUserLogin(userName)
        except Exception as e:
            raise e
            statusCode = 400
            statusMessage = 'Bad request'
        self.set_status(statusCode)
        self.write(statusMessage)
