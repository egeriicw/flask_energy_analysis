#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import jsonify
from flask_restful import Resource

from application.database import db
from application.model import Account

class AccountListAPI(Resource):
    def get(self):
        return jsonify(accounts)

    def post(self):
        return jsonify({'accountlist': 'POST'})

class AccountAPI(Resource):
    def get(self, id):
        return jsonify({'account': str(id)})

    def post(self, id):
        pass

    def delete(self, id):
        pass

class AccountServicesAPI(Resource):
    def get(self, id):
        return jsonify({'account_services': str(id)})
