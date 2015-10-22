# -*- coding: utf-8 -*-

from flask import jsonify
from flask_restful import Resource, reqparse, fields, marshal
from application.model import User
from application.database import db



class RegisterAPI(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('username', type=str, required=True)
        self.reqparse.add_argument('password', type=str, required=True)

        super(RegisterAPI, self).__init__()

    def post(self):
        args = self.reqparse.parse_args()

        user = User(username = args['username'])
        user.set_password(args['password'])

        try:
            db.session.add(user)
            db.session.commit()
            print "saved"
            status = True
        except:
            raise
            status = False
        db.session.close()
        return jsonify({'result': status})
