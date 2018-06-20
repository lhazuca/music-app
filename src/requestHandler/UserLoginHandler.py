import json
import tornado.web

class UserLoginHandler(tornado.web.RequestHandler):

    #update
    def put(self, userName):

        statusCode = 200
        statusMessage = 'User Updated'
        try:
            password = json.loads(self.request.body.decode('utf-8'))
            self.application.db.updateUserCredentials(userName, password)
        except Exception as e:
            raise e
            statusCode = 400
            statusMessage = "User was not updated"
        self.set_status(statusCode)
        self.write(statusMessage)
