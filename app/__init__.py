from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_migrate import Migrate
from flask_mail import Mail
from config import config


bootstrap = Bootstrap5()
db = SQLAlchemy()
session = Session()
migrate = Migrate()
mail = Mail()


def create_app(config_name="development"):
    """Creates a new Flask app using the Factory Pattern"""
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    db.init_app(app)
    session.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app
