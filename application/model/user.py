# -*- coding: utf-8 -*-

import os

from hashlib import sha256
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)
from sqlalchemy.types import Integer, String, DateTime, Boolean, Numeric

from application.database import db


class User(db.Model):

    """
    User definition

    """

    __tablename__ = 'users'
    __searchable_columns__ = ['name']

    id = db.Column(Integer, autoincrement=True, primary_key=True)

    # Core information
    first_name = db.Column(String(32), nullable=True)
    last_name = db.Column(String(32), nullable=True)
    email = db.Column(String(32), nullable=True)

    # Username
    username = db.Column(String(32), nullable=False)

    # Salted and hashed password
    _password = db.Column(String(64), nullable=False)

    admin = db.Column(Boolean, nullable=False, default=False)

    def _hash_password(self, password):
        if isinstance(password, unicode):
            password = password.encode('utf-8')
        salt = sha256()
        salt.update(os.urandom(60))
        hash = sha256()
        hash.update(password + salt.hexdigest())
        password = salt.hexdigest() + hash.hexdigest()

        if not isinstance(password, unicode):
            password = password.decode('utf-8')
        return password

    def verify_password(self, password):
        return (self._password == self._hash_password(password))

    def _generate_auth_token(self, expiration=600):
        s = Serializer(app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'id': self.id})

    def set_password(self, password):
        self._password = self._hash_password(password)

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None
        except BadSignature:
            return None
        user = User.query.get(data['id'])
        return user

    def __init__(self, *args, **kw):
        super(User, self).__init__(*args, **kw)

    def __repr__(self):
        return ('<User: username=%s, password=%s>' % (self.username, self._password)).encode('unicode_escape')

    def __unicode__(self):
        return self.username
"""
    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = self._hash_password(password)

    @classmethod
    def _hash_password(cls, password):
        if isinstance(password, unicode):
            password = password.encode('utf-8')
        salt = sha256()
        salt.update(os.urandom(60))
        hash = sha256()
        hash.update(password + salt.hexdigest())
        password = salt.hexdigest() + hash.hexdigest()

        if not isinstance(password, unicode):
            password = password.decode('utf-8')
        return password

    def validate_password(self, password):
        if not self.password or not password:
            return False

        hash = sha256()
        if isinstance(password, unicode):
            password = password.encode('utf-8')
        hash.update(password + str(self.password[:64]))
        return self.password[:64] == hash.hexdigest()
"""
