#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import jsonify
from flask_restful import Resource

class PlaceListAPI(Resource):
    def get(self):
        return jsonify({'placelist':'GET'})

    def post(self):
        return jsonify({'placelist': 'POST'})

class PlaceAPI(Resource):
    def get(self, id):
        return jsonify({'place': str(id)})

    def post(self, id):
        pass

    def delete(self, id):
        pass
