from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
import os
from flask_msearch import Search
from flask_login import LoginManager
#from dotenv import dotenv_values, load_dotenv


app = Flask(__name__)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
search = Search()
search.init_app(app)

# запрашивает местоположение файла(адрес), в котором выполняется код
BASEDIR = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
app.config['SECRET_KEY']='27hkmgBJvmvQdIC1poA2W3Cr99n_2zpmNqhKTn7tuds4TWCck'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(BASEDIR, 'static/images')

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)
#load_dotenv('e_shop/.env')
#key = app.dotenv_values(".env")["SECRET_KEY"]
#sql_alchemy_database = app.dotenv_values(".env")["SQLALCHEMY_DATABASE_URI"]
#sql_alchemy_track = app.dotenv_values(".env")["SQLALCHEMY_TRACK_MODIFICATIONS"]
#photos_upload = app.dotenv_values(".env")["UPLOADED_PHOTOS_DEST"]

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view='customerLogin'
login_manager.needs_refresh_message_category='danger'
login_manager.login_message = u"Please login first"

