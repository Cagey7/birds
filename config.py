class Config:
    """ Class with common configurations for all applications """

    SECRET_KEY = "very very hard to guess secret key"
    SESSION_TYPE = "filesystem"
    SESSION_PERMANENT = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    """ Devolopment configuration class """

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///C:\\home\\birds\\databases\\development.sqlite"


class ProductionConfig(Config):
    """ Production configuration class """

    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///C:\\home\\birds\\databases\\production.sqlite"


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig
}
