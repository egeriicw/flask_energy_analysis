# -*- coding: utf-8 -*-

from datetime import datetime

from sqlalchemy.types import Integer, String, DateTime, Boolean, Numeric

from application.database import db

class Account(db.Model):
    __tablename__ = 'accounts'
    __searchable_columns__ = ['uid']
    __search_detail_columns__ = ['']

    id = db.Column(Integer, autoincrement=True, primary_key=True)
    uid = db.Column(String(255), unique=True, nullable=False)
    type_id = db.Column(Integer, nullable=False) # convert to foreign key
    resource_id = db.Column(Integer, nullable=False) # convert to foreign key
    utility_id = db.Column(Integer, nullable=False) # convert to foreign key
    created = db.Column(DateTime, nullable=False, default=datetime.utcnow)
    active = db.Column(Boolean, nullable=False)

    def __unicode__(self):
        return self.uid

    def is_writable(self, user):
#        return user and (self.id == user.id or user.is_manager())
        pass

    def __init__(self, uid=None, type_id=None, resource_id=None, utility_id=None, active=False):
        self.uid = uid
        self.type_id = type_id
        self.resource_id = resource_id
        self.utility_id = utility_id
        self.active = active
