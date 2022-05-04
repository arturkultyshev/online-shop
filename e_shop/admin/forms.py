from wtforms import StringField, PasswordField, validators, ValidationError
from flask_wtf import FlaskForm
from .models import User


# https://flask.palletsprojects.com/en/2.1.x/patterns/wtforms/?highlight=forms
class RegistrationForm(FlaskForm):
    name = StringField('Name', [validators.Length(min=4,max=25)])
    username = StringField('Username', [validators.Length(min=4,max=25)])
    email = StringField('Email Address', [validators.Length(min=6,max=35)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')