#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import jsonify
from flask_restful import Api

from .accounts import AccountListAPI, AccountAPI, AccountServicesAPI
from .meters import MeterListAPI, MeterAPI, MeterDataAPI
from .places import PlaceListAPI, PlaceAPI
from .users import UserListAPI, UserAPI
from .template import TemplateAPI
from .authentication import LoginAPI, RegisterAPI


import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def init_api(app):
    #app = Flask(__name__)
    api = Api()
    api.add_resource(TemplateAPI, '/')
    api.add_resource(AccountListAPI, '/accounts/', endpoint='accounts')
    api.add_resource(AccountAPI, '/accounts/<int:id>', endpoint='account')
    api.add_resource(AccountServicesAPI, '/accounts/<int:id>/services', endpoint='accountservices')
    api.add_resource(MeterListAPI, '/meters/', endpoint='meters')
    api.add_resource(MeterAPI, '/meters/<int:id>', endpoint='meter')
    api.add_resource(MeterDataAPI, '/meters/<int:id>/data', endpoint='meterdata')
    api.add_resource(PlaceListAPI, '/places/', endpoint='places')
    api.add_resource(PlaceAPI, '/places/<int:id>', endpoint='place')
    api.add_resource(UserListAPI, '/users/', endpoint='users')
    api.add_resource(UserAPI, '/users/<int:id>', endpoint='user')
    api.add_resource(LoginAPI, '/auth/login', endpoint='login')
    api.add_resource(RegisterAPI, '/auth/register', endpoint='register')

    api.init_app(app)
    return app
