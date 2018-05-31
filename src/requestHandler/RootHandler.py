import tornado.web

class RootHandler(tornado.web.RequestHandler):

    def get(self):
        self.set_status(200)
        self.write("Welcome to API")