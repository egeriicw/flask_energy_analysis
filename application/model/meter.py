# -*- coding: utf-8 -*-

from datetime import datetime

from sqlalchemy.types import Integer, String, DateTime, Boolean, Numeric

from application.database import db

class Meter(db.Model):
    __tablename__ = 'meters'
    __searchable_columns__ = ['meter_number']
    __search_detail_columns__ = ['']

    id = db.Column(Integer, autoincrement=True, primary_key=True)
    meter_number = db.Column(String(255), unique=True, nullable=False)
    meter_type_id = db.Column(Integer, nullable=False) # convert to foreign key
    meter_resource_id = db.Column(Integer, nullable=False) # convert to foreign key
    date_created = db.Column(DateTime, nullable=False, default=datetime.utcnow)
    active = db.Column(Boolean, nullable=False)

    def __unicode__(self):
        return self.meter_number

    def is_writable(self, user):
#        return user and (self.id == user.id or user.is_manager())
        pass

class MeterData(db.Model):
    __tablename__ = 'meterdata'
    __searchable_columns__ = ['start_datetimestamp', 'end_datetimestamp']
    __search_detail_column = ['value']

    id = db.Column(Integer, autoincrement=True, primary_key=True)
    start_datetimestamp = db.Column(DateTime, nullable=False)
    end_datetimestamp = db.Column(DateTime, nullable=False)
    value = db.Column(Numeric, nullable=False, default=0.0)

    def __unicode__(self):
        return self.start_datetimestamp, self.end_datetimestamp, self.value

    def __repr__(self):
        pass
