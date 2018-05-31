import sys
from os import getcwd
sys.path.insert(0, getcwd())
import tornado.httpserver
from tornado.ioloop import IOLoop
from src.Application import Application


def runServer():
    server = tornado.httpserver.HTTPServer(Application())
    server.listen(8080)
    print("Server listen on 8080")
    IOLoop.instance().start()

if __name__ == "__main__":

    runServer()
