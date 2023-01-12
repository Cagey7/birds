from flask import render_template, redirect, url_for, flash, session, request
from flask_login import login_user, logout_user, current_user
from ..email import send_email
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


@auth.route("/reset/<token>", methods=["GET", "POST"])
def password_reset(token):
    form = ResetPasswordForm()
    if form.validate_on_submit():
        if User.reset_password(token, form.password.data):
            flash("Your password has been updated")
            return redirect(url_for("auth.login"))
        else:
            print("tesetet")
            flash("Probably your token is too old")
            return redirect(url_for("auth.login"))
    return render_template("auth/reset.html", form=form, token=token)


@auth.route("/reset", methods=["GET", "POST"])
def password_reset_request():
    if not current_user.is_anonymous:
        return redirect(url_for("main.index"))
    form = PassrecoveryForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data.lower()).first()
        if user:
            token = user.generate_reset_token()
            send_email(form.email.data, "Reset password", "mail/reset", token=token)
            flash("Check your email to change password")
            return redirect(url_for("auth.login"))
        else:
            flash("User with this email doesn't exist")
            return redirect(url_for("auth.password_reset_request"))
    return render_template("auth/resetrequest.html", form=form)
