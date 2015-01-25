import tornado.ioloop
import tornado.web
import tornado.httpclient
import tornado.gen
import json

g_access_token = ""
g_client_id = 23079608
g_client_secret = "f4727f20522e2394ad8813381ce7f457"

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # self.write("Good morning,dacy!")
        t_url = "https://oauth.taobao.com/authorize?response_type=code&client_id=23079608&redirect_uri=127.0.0.1:8888/starthandler"
        self.redirect(t_url)
    # def get(self):
    #     self.write('<form action="/" method="post">'
    #         '<input name="message" type="text" />'
    #         '<input type="submit" value="Submit" />'
    #         '</form> ')
    # def post(self):
    #     self.set_header("Content-Type", "text/plain")        
    #     self.write("You wrote " + self.get_argument("message"))
    def post(self):
        self.write("hello,post")

# ==============================FUNC FOR CALLBACK================================================= #
# def handle_request(response):
#   global g_access_token
#   '''callback needed when a response arrive'''
#   if response.error:
#     print "Error:", response.error
#   else:
#     print 'called'
#     print response.body
#     g_access_token = response.body["access_token"]

class StartHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        # self.write("Good morning,dacy!")
        self.request.method = "POST"
        t_code = self.get_argument("code")
        # t_url = "https://oauth.taobao.com/token"
        t_url = "https://oauth.taobao.com/token?client_id=23079608&client_secret=f4727f20522e2394ad8813381ce7f457&grant_type=authorization_code&code=%s&redirect_uri=127.0.0.1:8888/starthandler"%t_code
        # self.redirect(t_url)
        t_body = json.dumps({"client_id":str(g_client_id),"client_secret":g_client_secret,"grant_type":"authorization_code","code":str(t_code),"redirect_uri":"127.0.0.1:8888/starthandler"})
        # self.write("<script>window.location.href='%s';</script>"%t_url)
        t_httpclient = tornado.httpclient.AsyncHTTPClient()
        # t_httpclient = tornado.httpclient.HTTPClient()
        t_request = tornado.httpclient.HTTPRequest(url=t_url,method="POST",body=t_body)
        t_response =yield t_httpclient.fetch(t_request)
        import pdb;pdb.set_trace()
        print t_response.body
        t_resp = json.loads(t_response.body.decode('utf8'))
        g_access_token = t_resp["access_token"]
        print("====>>",g_access_token)
        
        # t_response = t_httpclient.fetch(t_request,handle_request)
        t_httpclient.close()
    def post(self):
        self.write("hello")

app = tornado.web.Application\
    ([
    (r"/",MainHandler),
    (r"/starthandler",StartHandler),
    ])

if __name__ == '__main__':
    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
