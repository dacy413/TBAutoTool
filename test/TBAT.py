import tornado.ioloop
import tornado.web
import tornado.httpclient
import tornado.gen
import json
import threading
import ConfigParser

import TBATHandler

g_access_token = ""
g_client_id = 23079608
g_client_secret = "f4727f20522e2394ad8813381ce7f457"
# g_callback_url = "127.0.0.1:8888/starthandler"
g_callback_url = "121.41.55.86:8800/starthandler"
g_config = ConfigParser.ConfigParser()
g_config.read("config.ini")

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # self.write("Good morning,dacy!")
        t_url = "https://oauth.taobao.com/authorize?response_type=code&client_id=%s&redirect_uri=%s"\
        %(str(g_client_id),g_callback_url)
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
    global g_config

    @tornado.gen.coroutine
    def get(self):
        # self.write("Good morning,dacy!")
        self.request.method = "POST"
        t_code = self.get_argument("code")
        # t_url = "https://oauth.taobao.com/token"
        t_url = "https://oauth.taobao.com/token?client_id=%s&client_secret=%s&grant_type=authorization_code&code=%s&redirect_uri=%s"\
        %(g_client_id,g_client_secret,t_code,g_callback_url)
        # self.redirect(t_url)
        t_body = json.dumps({"client_id":str(g_client_id),"client_secret":g_client_secret,"grant_type":"authorization_code","code":str(t_code),"redirect_uri":str(g_callback_url)})
        # self.write("<script>window.location.href='%s';</script>"%t_url)
        t_httpclient = tornado.httpclient.AsyncHTTPClient()
        # t_httpclient = tornado.httpclient.HTTPClient()
        t_request = tornado.httpclient.HTTPRequest(url=t_url,method="POST",body=t_body)
        t_response =yield t_httpclient.fetch(t_request)
        # import pdb;pdb.set_trace()
        # print t_response.body
        t_resp = json.loads(t_response.body.decode('utf8'))
        g_access_token = t_resp["access_token"]
        logger.log(2,"====>>ACCESS_TOKEN:%s"%g_access_token)
        # print("====>>ACCESS_TOKEN:%s"%g_access_token)
        # t_response = t_httpclient.fetch(t_request,handle_request)
        t_httpclient.close()
        # print("====>>START NEW THREAD...")
        if g_config.get("app","run_mode"):
            new_thread = threading.Thread(target = TBATHandler.send_goods,args = (str(g_client_id),str(g_client_secret),str(g_access_token)))
            new_thread.setDaemon(True)
            new_thread.start()
            logger.log(2,"====>>NEW THREAD RUNING...")
        else:
            g_config.set("app","access_token",str(g_access_token))
        self.write("<h1><center>YES,AUTO SEND GOODS SERVER IS RUNING...</center></h1>")

    def post(self):
        self.write("hello")

app = tornado.web.Application\
    ([
    (r"/",MainHandler),
    (r"/starthandler",StartHandler),
    ])

if __name__ == '__main__':
    app.listen(8800)
    tornado.ioloop.IOLoop.instance().start()
