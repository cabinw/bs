#-*- coding: UTF-8 -*- 
import tornado.ioloop
from tornado.options import define, options, logging
import tornado.web
import unittest
from jinja2 import Environment, PackageLoader
import os
define("port", default=8888, help="run on the given port", type=int)

settings = {
    "debug": True,
}

server_settings = {
    "xheaders" : True,

}

class Test(unittest.TestCase):
    
    consumer_key= "2886103344"
    consumer_secret ="87e807bec7a2481728646d3f1c1459f1"
    
    def __init__(self):
            """ constructor """
    
    def getAtt(self, key):
        try:
            return self.obj.__getattribute__(key)
        except Exception, e:
            print e
            return ''
        
    def getAttValue(self, obj, key):
        try:
            return obj.__getattribute__(key)
        except Exception, e:
            print e
            return ''
        
    def auth(self):
        self.auth = OAuthHandler(self.consumer_key, self.consumer_secret)
        auth_url = self.auth.get_authorization_url()
        print 'Please authorize: ' + auth_url
        verifier = raw_input('PIN: ').strip()
        self.auth.get_access_token(verifier)
        self.api = API(self.auth)
     
    def setToken(self, token, tokenSecret):
        self.auth = OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.setToken(token, tokenSecret)
	self.api = API(self.auth)
    
    def update(self, message):
        message = message.encode("utf-8")
        status = self.api.update_status(status=message, lat="22.512556954051437", long="114.169921875")
        self.obj = status
        id = self.getAtt("id")
        text = self.getAtt("text")
        print "update---"+ str(id) +":"+ text
        
    def destroy_status(self, id):
        status = self.api.destroy_status(id)
        self.obj = status
        id = self.getAtt("id")
        text = self.getAtt("text")
        print "update---"+ str(id) +":"+ text

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # env = Environment(loader=PackageLoader('yourapplication', 'templates'))
        # template = env.get_template('mytemplate.html')
        url1 = {'name':'google','url':'http://www.google.com'}
        url2 = {'name':'163','url':'http://www.163.com'}
        items = [url1,url2]
        self.render("start.html", title="My title", items=items)
        # print template.render(the='variables', go='here'

def main():
    settings = dict(
            static_path = os.path.join("static")
        )
    tornado.options.parse_command_line()
    logging.info("Starting Tornado web server on http://localhost:%s" % options.port)
    application = tornado.web.Application([
        (r"/", MainHandler),
    ], **settings)
    application.listen(options.port, **server_settings)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
