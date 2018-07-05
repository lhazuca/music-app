import json
from src.requestHandler.BaseHandler import BaseHandler

class UserLogoutHandler(BaseHandler):

    def post(self):
        statusCode = 200
        statusMessage = 'User logged-out'
        try:
            data = json.loads(self.request.body.decode('utf-8'))
            userName = data['userName']
            if self.isLoggendin(userName):
                self.application.db.loggoutUser(userName)
        except Exception as e:
            #raise e
            statusCode = 400
            statusMessage = "User not logged-out"
        self.set_status(statusCode)
        self.write(statusMessage)