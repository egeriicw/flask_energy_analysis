#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import jsonify
from flask_restful import Resource

class UserListAPI(Resource):
    def get(self):
        return jsonify({'userlist':'GET'})

    def post(self):
        return jsonify({'userlist': 'POST'})

class UserAPI(Resource):
    def get(self, id):
        return jsonify({'user': str(id)})

    def post(self, id):
        pass

    def delete(self, id):
        pass
