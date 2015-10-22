#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import config

from flask import Flask, request, g
from config import config

class Application(Flask):

    def __init__(self, name='Application', config_file=None, *args, **kw):
        # Create Flask instance
        super(Application, self).__init__(name, *args, **kw)

        #self.config.from_pyfile(config.DEFAULT_CONF_PATH)

        if config_file:
            self.config.from_pyfile(config_file)

    def add_sqlalchemy(self):
        """ Create and configure SQLAlchemy extension """
        from application.database import db, migrate
        db.init_app(self)
        migrate.init_app(self, db)

    def add_api(self):
        """Create and configure API """
        from application.api import init_api
        return init_api(self)

def create_app(*args, **kw):
    app = Application(*args, **kw)
    app.config.from_object(config.config['dev'])
    app.add_sqlalchemy()
    app.add_api()
    return app
