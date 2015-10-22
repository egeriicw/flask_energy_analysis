from flask import Blueprint

core = Blueprint('core', __name__)
analysis = Blueprint('analysis', __name__, url_prefix='/analysis')
accounts = Blueprint('accounts', __name__, url_prefix='/accounts')
auth = Blueprint('auth', __name__, url_prefix='/auth')
admin = Blueprint('admin', __name__, url_prefix='/admin')

def register_apps(app):
    app.register_blueprint(core)
    app.register_blueprint(analysis)
    app.register_blueprint(accounts)
    app.register_blueprint(auth)
    app.register_blueprint(admin)
    return app

import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from flask import Flask, request

@core.route("/", methods=['GET'])
def main():
    return json.dumps({'status': 'main'})

@analysis.route('/', methods=['GET'])
def analytics():
    return json.dumps({'status': 'analysis'})

@accounts.route('/', methods=['GET'])
def account_list():
    return json.dumps({'status': 'accounts'})

@auth.route("/login/", methods=['GET', 'POST'])
def auth_login():
    return json.dumps({'status': 'auth/login'})

@auth.route("/logout/", methods=['GET', 'POST'])
def auth_logout():
    return json.dumps({'status': 'auth/logout'})

@auth.route('/register/', methods=['GET', 'POST'])
def auth_register():
    return json.dumps({'status': 'auth/register'})

@admin.route('/', methods=['GET'])
def admin_login():
    return json.dumps({'status': 'admin'})


def create_app():
    app = Flask(__name__)
    app = register_apps(app)
    return app
