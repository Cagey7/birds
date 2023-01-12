from flask import render_template, redirect, url_for, flash, session, request
from flask_login import login_user, logout_user
from .forms import *
from . import auth
from .. import db


@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data.lower()).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, True)
            return redirect(request.args.get("next") or url_for("main.index"))
        flash("Wrong email or password", "error")
        return redirect(url_for("auth.login"))
    return render_template("auth/login.html", form=form)


@auth.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data.lower(),
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("auth.login"))
    return render_template("auth/register.html", form=form)


@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.index"))


@auth.route("/reset", methods=["GET", "POST"])
def reser():
    form = ResetPasswordForm()
    if form.validate_on_submit():
        email = "admin@gmail.com"
        user = User.query.filter_by(email=email).first()
        token = user.generate_reset_token()
        User.reset_password(token, form.password.data)
        
    return render_template("auth/reset.html", form=form)


@auth.route("/passrecovery", methods=["GET", "POST"])
def passrecovery():
    email = "no"
    form = PassrecoveryForm()
    if form.validate_on_submit():
        email = form.email.data
    return render_template("auth/passrecovery.html", form=form, email=email)
