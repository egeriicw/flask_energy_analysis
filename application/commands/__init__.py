#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask.ext.script import Manager
from flask.ext.migrate import MigrateCommand

from .server import Server, APIServer
from .shell import Shell

from application.app import create_app

def _create_app(config=None):
    app = create_app()
    return app

manager = Manager(_create_app)
manager.add_option('-c', '--config', dest='config', required=False)
manager.add_command("runserver", Server(use_debugger=True, use_reloader=True, host='0.0.0.0', port='8000'))
manager.add_command("run_api_server", APIServer(host='0.0.0.0', port='5001'))
manager.add_command("shell", Shell())
manager.add_command("db", MigrateCommand)
