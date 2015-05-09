
import sys
reload(sys)
sys.setdefaultencoding("utf8")

import os.path
import re
# import torndb
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

from handlers.handler import MainHandler,SubscribeHandler
import uimodules

# define("port", default = 80, type = int)
# define("mysql_host", default = "127.0.0.1")
# define("mysql_database", default = "knewone")
# define("mysql_user", default = "root")
# define("mysql_password", default = "daoli123")

class Application(tornado.web.Application):
    def __init__(self):
        settings = dict(
            template_path = os.path.join(os.path.dirname(__file__), "templates"),
            static_path = os.path.join(os.path.dirname(__file__), "static"),
           # xsrf_cookies = True,
            cookie_secret = "cookie_secret_code",
            login_url = "/login",
            ui_modules = uimodules,
        )

        handlers = [
            (r"/",MainHandler),
	        (r"/",SubscribeHandler),
        ]

        tornado.web.Application.__init__(self, handlers, **settings)

        # self.db = torndb.Connection(
        #     host = options.mysql_host, database = options.mysql_database,
        #     user = options.mysql_user, password = options.mysql_password
        # )

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    # http_server.listen(options.port)
    http_server.listen(999)
    tornado.ioloop.IOLoop.instance().start()

