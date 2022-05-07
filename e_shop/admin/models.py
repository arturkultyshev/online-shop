from e_shop import db


'''https://flask.palletsprojects.com/en/2.1.x/patterns/wtforms/?highlight=forms'''
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=False, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(180), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


db.create_all()
