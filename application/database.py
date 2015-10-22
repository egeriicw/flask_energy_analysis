# -*- coding: utf-8 -*-

from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate

def query(cls, **kw):
    q = db.session.query(cls)

    if kw:
        q = q.filter_by(**kw)

    return q

def query_first(cls, **kw):
    q = db.session.query(cls)

    if kw:
        q = q.filter_by(**kw)

    return q.first()

def get(cls, id):
    return cls.query().get(id)


def exists(cls, **kw):
    return cls.query(**kw).first() is not None

def save(cls):
    db.session.add(cls)
    db.session.commit()

def close(cls):
    db.session.close()

db = SQLAlchemy(session_options=dict(expire_on_commit=False))
migrate = Migrate()

db.Model.flask_query = db.Model.query
db.Model.query = classmethod(query)
db.Model.get = classmethod(get)
db.Model.exists = classmethod(exists)
db.Model.save = classmethod(save)
db.Model.close = classmethod(close)
db.Model.query_first = classmethod(query_first)
