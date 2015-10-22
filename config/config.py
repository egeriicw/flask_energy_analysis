#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

class BaseConfig(object):
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    CSRF_ENABLED = True
    CSRF_SESSION_KEY = "secret"
    # SECRET_KEY = os.urandom(16).encode('hex')
    SECRET_KEY = os.getenv('SECRET_KEY', None)

class DevConfig(BaseConfig):
    DEBUG = os.getenv('DEBUG', True)
    #SQLALCHEMY_DATABASE_USER = os.environ.get()
    #SQLALCHEMY_DATABASE_PASSWORD = os.environ.get()
    #SQLALCHEMY_DATABASE_DBNAME = os.environ.get()
    DATABASE_USER = os.getenv('DATABASE_USER', 'postgres')
    DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', 'postgres')
    DATABASE_HOST = os.getenv('DB_1_PORT_5432_TCP_ADDR', 'localhost')
    DATABASE_PORT = os.getenv('DATABASE_PORT', '5432')
    DATABASE_NAME = os.getenv('DATABASE_NAME', 'application_dev')

    SQLALCHEMY_DATABASE_URI = "postgresql://{0}:{1}@{2}:{3}/{4}".format(DATABASE_USER, DATABASE_PASSWORD, DATABASE_HOST, DATABASE_PORT, DATABASE_NAME)

class TestConfig(BaseConfig):
    DEBUG = os.getenv('DEBUG', True)
    #SQLALCHEMY_DATABASE_USER = os.environ.get()
    #SQLALCHEMY_DATABASE_PASSWORD = os.environ.get()
    #SQLALCHEMY_DATABASE_DBNAME = os.environ.get()
    #SQLALCHEMY_DATABASE_USER = 'postgres'
    #SQLALCHEMY_DATABASE_PASSWORD = 'postgres'
    #SQLALCHEMY_DATABASE_DBNAME = 'application_test'

    #SQLALCHEMY_DATABASE_URI = "postgresql://{0}:{1}@localhost/{2}".format(SQLALCHEMY_DATABASE_USER, SQLALCHEMY_DATABASE_PASSWORD, SQLALCHEMY_DATABASE_DBNAME)

class ProdConfig(BaseConfig):
    DEBUG = os.getenv('DEBUG', False)
    #SQLALCHEMY_DATABASE_USER = os.environ.get()
    #SQLALCHEMY_DATABASE_PASSWORD = os.environ.get()
    #SQLALCHEMY_DATABASE_DBNAME = os.environ.get()
    #SQLALCHEMY_DATABASE_USER = 'postgres'
    #SQLALCHEMY_DATABASE_PASSWORD = 'postgres'
    #SQLALCHEMY_DATABASE_DBNAME = 'application_prod'

    #SQLALCHEMY_DATABASE_URI = "postgresql://{0}:{1}@localhost/{2}".format(SQLALCHEMY_DATABASE_USER, SQLALCHEMY_DATABASE_PASSWORD, SQLALCHEMY_DATABASE_DBNAME)

config = {
    'dev': DevConfig,
    'test': TestConfig,
    'prod': ProdConfig,
}
