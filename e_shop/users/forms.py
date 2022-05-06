from wtforms import StringField, PasswordField, SubmitField,\
    validators, ValidationError
from flask_wtf import FlaskForm
from .model import Register


# форма регистрации в которой присутствуют такие поля как имя,
# логин, почта, пароль, подтверждение пароля.
class CustomerRegisterForm(FlaskForm):
    name = StringField('Name: ')
    username = StringField('Username: ', [validators.DataRequired()])
    email = StringField('Email: ', [validators.Email(), validators.DataRequired()])
    password = PasswordField('Password: ', [validators.DataRequired(),
            validators.EqualTo('confirm', message=' Пароли не совпадают! ')])
    confirm = PasswordField('Repeat Password: ', [validators.DataRequired()])
    submit = SubmitField('Register')


# функция для проверки повторения логина при регистрации.
# Не может существовать два одинаковых логина
    def validate_username(self, username):
        if Register.query.filter_by(username=username.data).first():
            raise ValidationError("Этот логин уже существует!")


# функция для проверки повторения почты при регистрации.
    def validate_email(self, email):
        if Register.query.filter_by(email=email.data).first():
            raise ValidationError("Данная почта уже существует!")


class CustomerLoginFrom(FlaskForm):
    email = StringField('Email: ', [validators.Email(), validators.DataRequired()])
    password = PasswordField('Password: ', [validators.DataRequired()])
