import os
from dotenv import load_dotenv
load_dotenv()


class Config:
    """Class with common configurations for all applications"""
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SESSION_TYPE = "filesystem"
    SESSION_PERMANENT = False
    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    """Devolopment configuration class"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_SQLALCHEMY_DATABASE_URI")


class ProductionConfig(Config):
    """Production configuration class"""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("PROD_SQLALCHEMY_DATABASE_URI")


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig
}
