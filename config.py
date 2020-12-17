import os

class Config: 
    '''
    General configuration for parent class
    '''
    SECRET_KEY='5ee0b946c852fa4827b3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://access:Access@localhost/blogs'

    # email configurations
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'Personal Blog'
    #SENDER_EMAIL = 'eidabdullahi10@gmail.com'

    # simple mde configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True


    @staticmethod
    def init_app(app):
        pass

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

    '''
    Production configuration for child class
    '''
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://access:Access@localhost/blogs_test'


class DevConfig(Config):
    '''
    Development configuration for child class
    '''
    class DevConfig(Config):
        SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://access:Access@localhost/blogs'
    DEBUG = True

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}