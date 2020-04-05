import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    # Psycopg : Python adapter of PostgreSQSL database
    # Adapt Python types to PostgreSQSL types.
    # While doing so, database will be connected to the application.
    # This will occure into models.py.

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class DevelopmentConfig(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
