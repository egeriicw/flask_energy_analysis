# -*- coding: utf-8 -*-

from flask.ext.script import Server as BaseServer

class Server(BaseServer):
    def handle(self, app, *args, **kw):
#        app = create_combined_app()
        super(Server, self).handle(app, *args, **kw)

class APIServer(BaseServer):
    def handle(self, app, *args, **kw):
#        app = create_combined_app()
        super(Server, self).handle(app, *args, **kw)
