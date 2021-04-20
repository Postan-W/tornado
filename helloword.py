"""
@Time : 2021/4/20 17:51
@Author : wmingzhu
@Annotation : 
"""
import tornado.ioloop
import tornado.web

class Handler(tornado.web.RequestHandler):
    def get(self):
        self.write("this is my tornado template")

def make_app():
    return tornado.web.Application([(r"/basicGet",Handler),])

if __name__ == "__main__":
    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
