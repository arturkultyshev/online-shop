import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Products(SqlAlchemyBase):
    __tablename__ = 'items'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name_of_product = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    manufacturer = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    number_of_items = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    cost_of_item = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    image = sqlalchemy.Column(sqlalchemy.String, nullable=False)

