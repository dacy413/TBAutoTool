import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # self.write("Good morning,dacy!")
        tmp_str = "https://oauth.taobao.com/authorize?response_type=token&client_id=23079608&redirect_uri=127.0.0.1:8888/starthandler"
        self.redirect(tmp_str)

class StartHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Good morning,dacy!")

app = tornado.web.Application\
    ([
    (r"/",MainHandler),
    (r"/starthandler",StartHandler),
    ])

if __name__ == '__main__':
    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
