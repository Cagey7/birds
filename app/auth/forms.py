from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from app.models import User


class LoginForm(FlaskForm):
    """ Flask wtf login class """

    email = StringField("Email", validators=[DataRequired("Email is required"), Length(1, 64), Email("Wrong email format")])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Log in")


class RegistrationForm(FlaskForm):
    """ Flask wth registration class """

    email = StringField("Email", validators=[DataRequired(), Length(1, 64), Email("Wrong email format")])
    username = StringField("Username", validators=[DataRequired(), Length(1, 64), Regexp("^[A-Za-z][A-Za-z0-9_.]*", 
                                        flags=0, 
                                        message="Usernames must have only letters, numbers, dots or underscores")])
    password = PasswordField("Password", validators=[DataRequired(), EqualTo("confirm_password", message="Passwords must match.")])
    confirm_password = PasswordField("Confirm password", validators=[DataRequired()])
    submit = SubmitField("Register")


    def validate_email(self, field):
        """ Checks if email is already taken """
        if User.query.filter_by(email=field.data.lower()).first():
            raise ValidationError("Email already registered.")
    

    def validate_username(self, field):
        """ Checks if username is already taken """
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("Username already in used.")
