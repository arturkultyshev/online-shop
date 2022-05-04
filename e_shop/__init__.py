from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
import os
from flask_msearch import Search
from flask_login import LoginManager


app = Flask(__name__)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
search = Search()
search.init_app(app)
# запрашивает местоположение файла(адрес), в котором выполняется код
BASEDIR = os.path.abspath(os.path.dirname(__file__))
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view='customerLogin'
login_manager.needs_refresh_message_category='danger'
login_manager.login_message = u"Please login first"

