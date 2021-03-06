from e_shop import db, login_manager
from datetime import datetime
from flask_login import UserMixin
import json


@login_manager.user_loader
def user_loader(user_id):
    return Register.query.get(user_id)


# создание формы для регистрации для базы данных.
# Столбцы: айди, имя, логин, пароль, почта, дата создания.
@login_manager.user_loader
def user_loader(user_id):
    return Register.query.get(user_id)


# создание бд строк для регистрации.
# Столбцы: айди, имя, логин, почта, пароль, дата создания
class Register(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=False)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(200), unique=False)
    date_created = db.Column(db.DateTime, nullable=False,
                             default=datetime.utcnow)


    def __repr__(self):
        return '<Register %r>' % self.name

"""реализация пользовательского типа:"""
class JsonEcodedDict(db.TypeDecorator):
    impl = db.Text
    """ https://stackoverflow.com/questions/45624009/how-to-get-original-value-of-sqlalchemy-custom-type"""
    def process_bind_param(self, value, dialect):
        if value is None:
            return '{}'
        else:
            return json.dumps(value)

    """
    https://stackoverflow.com/questions/45624009/how-to-get-original-value-of-sqlalchemy-custom-type
    """
    def process_result_value(self, value, dialect):
        if value is None:
            return {}
        else:
            return json.loads(value)


# создание модели для формирования заказа
class CustomerOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    invoice = db.Column(db.String(20), unique=True, nullable=False)
    status = db.Column(db.String(20), default='Pending', nullable=False)
    customer_id = db.Column(db.Integer, unique=False, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow,
                             nullable=False)
    orders = db.Column(JsonEcodedDict)


    def __repr__(self):
        return'<CustomerOrder %r>' % self.invoice

db.create_all()
