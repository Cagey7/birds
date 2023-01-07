from flask import render_template, session, abort, request, redirect, url_for
from . import main
from app.models import *

@main.route("/", methods=["GET", "POST"])
def index():
    session["username"] = None
    birds = None
    voted_bird = None
    if session["username"]:
        user_id = User.query.filter_by(username=session["username"]).first().id
        bird = Vote.query.filter_by(user_id=user_id).first()
        if bird:
            bird_id = bird.bird_id
            voted_bird = Bird.query.filter_by(id=bird_id).first()
    birds = Bird.query.all()
    return render_template("index.html", birds=birds, voted_bird=voted_bird)


@main.route("/profile/<username>")
def profile(username):
    voted_bird = None
    user_id = User.query.filter_by(username=session["username"]).first().id
    bird = Vote.query.filter_by(user_id=user_id).first()
    if bird:
        bird_id = bird.bird_id
        voted_bird = Bird.query.filter_by(id=bird_id).first()
    if not username == session["username"]:
        abort(404)
    return render_template("profile.html", voted_bird=voted_bird)


@main.route("/vote", methods=["GET", "POST"])
def vote():
    if request.form.get("vote"):
        user_id = User.query.filter_by(username=session["username"]).first().id
        bird_id = request.form.get("vote")
        vote = Vote(user_id=user_id, bird_id=bird_id)
        db.session.add(vote)
        db.session.commit()
    return redirect(url_for("main.index"))
