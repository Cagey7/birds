from flask import render_template, session, abort
from . import main

@main.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@main.route("/profile/<username>")
def profile(username):
    if not username == session["username"]:
        abort(404)
    return render_template("profile.html")
