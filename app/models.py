from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from . import db, login_manager
from flask_login import UserMixin


class User(db.Model, UserMixin):
    """Sqlalchemy user class"""
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(320), unique=True, nullable=False)
    password_hash = db.Column(db.String(500), nullable=False)
    vote = db.relationship("Vote", backref="user", uselist=False)


    @property
    def password(self):
        raise AttributeError("password is not a readable attribute")


    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self, password):
        """ Compare inputted password with password in database """
        return check_password_hash(self.password_hash, password)
    

    def generate_reset_token(self, expiration=3600):
        s = Serializer(current_app.config["SECRET_KEY"], expiration)
        return s.dumps({"reset": self.id})


    @staticmethod
    def reset_password(token, new_password):
        s = Serializer(current_app.config["SECRET_KEY"])
        try:
            data = s.loads(token)
        except:
            return False
        user = User.query.get(data.get("reset"))
        if user is None:
            return False
        user.password = new_password
        db.session.commit()
        return True


class Bird(db.Model):
    """Sqlalchemy bird class"""
    __tablename__ = "birds"
    id = db.Column(db.Integer, primary_key=True)
    species = db.Column(db.String(64), unique=True, nullable=False)
    info = db.Column(db.Text, nullable=False)
    image_path = db.Column(db.String(256), nullable=False)
    votes = db.relationship("Vote", backref="bird")


class Vote(db.Model):
    """Sqlalchemy vote class"""
    __tablename__ = "votes"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    bird_id = db.Column(db.Integer, db.ForeignKey("birds.id"))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
