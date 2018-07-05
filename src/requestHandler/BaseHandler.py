import tornado.web

class BaseHandler(tornado.web.RequestHandler):


    def isLoggendin(self,userName):
        return self.application.db.isLoggedin(userName)