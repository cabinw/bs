#-*- coding: UTF-8 -*- 
import tornado.ioloop
from tornado.options import define, options, logging
import tornado.web
import os
define("port", default=8888, help="run on the given port", type=int)

settings = {
    "debug": True,
}

server_settings = {
    "xheaders" : True,

}

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # env = Environment(loader=PackageLoader('yourapplication', 'templates'))
        # template = env.get_template('mytemplate.html')
        url1 = {'name':'google','url':'http://www.google.com'}
        url2 = {'name':'163','url':'http://www.163.com'}
        items = [url1,url2]
        self.render("start.html", title="My title", items=items)
        # print template.render(the='variables', go='here'
class BgHandler(tornado.web.RequestHandler):
    def get(self):
        file = open('static/bg.file')
        results = file.readlines()
        for i in range(0,len(results)):
            results[i] = results[i].strip()
        self.render("bg.html", title="My title", items=results)


def main():
    settings = dict(
            static_path = os.path.join("static")
        )
    tornado.options.parse_command_line()
    logging.info("Starting Tornado web server on http://localhost:%s" % options.port)
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/bg", BgHandler),
    ], **settings)
    application.listen(options.port, **server_settings)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
