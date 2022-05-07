from wtforms import StringField, PasswordField, validators, ValidationError
from flask_wtf import FlaskForm
from .models import User


'''
https://flask.palletsprojects.com/en/2.1.x/patterns/wtforms/?highlight=forms
'''
class RegistrationForm(FlaskForm):
    name = StringField('Name', [validators.Length(min=4, max=25)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')

    '''
    Пользовательскиq валидатор из модуля wtf.forms.
     Встроенный валидатор для проверки одного поля. 
    '''
    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')

    '''
    Встроенный валидатор для проверки одного поля. Если в приведенном
    ниже примере поле имени должно быть разделено на два поля для имени
    и фамилии, вам придется дублировать свою работу, чтобы проверить
    две длины.
    '''
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

'''
Все, что мы здесь сделали, это вывели точно такой же код из класса
и в качестве функции. Поскольку валидатором может быть любой вызываемый,
который принимает форму и поле двух позиционных аргументов,
это совершенно нормально, но валидатор очень специальный.
'''
class LoginForm(FlaskForm):
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [validators.DataRequired()])
