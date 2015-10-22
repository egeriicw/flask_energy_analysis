# -*- coding: utf-8 -*-

from flask import jsonify
from flask_restful import Resource, reqparse, fields, marshal
from application.model import User

class LoginAPI(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('username', type=str, required=True)
        self.reqparse.add_argument('password', type=str, required=True)

        super(LoginAPI, self).__init__()

    def post(self):
        args = self.reqparse.parse_args()

#        user = User.query(username=args['username']).first()
        user_exists = User.exists(username=args['username'])

        print user_exists

        if user_exists:
            u = User.query_first(username=args['username'])
            print u.verify_password(args['password'])
            if u.verify_password(args['password']):
                status = True
            else:
                print 'password'
                status = False
        else:
            print "user"
            status = False
        return jsonify({'result': status})
