from flask import render_template
from .forms import *
from . import auth


@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    return render_template("auth/login.html", form=form)


@auth.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    return render_template("auth/register.html", form=form)
