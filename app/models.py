from app import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(320), unique=True, nullable=False)
    password = db.Column(db.String(500), nullable=False)
    vote = db.relationship("Vote", backref="user", uselist=False)


class Bird(db.Model):
    __tablename__ = "birds"
    id = db.Column(db.Integer, primary_key=True)
    species = db.Column(db.String(64), unique=True, nullable=False)
    info = db.Column(db.Text, nullable=False)
    image_path = db.Column(db.String(256), nullable=False)
    birds = db.relationship("Vote", backref="bird")


class Vote(db.Model):
    __tablename__ = "votes"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    bird_id = db.Column(db.Integer, db.ForeignKey("birds.id"))
