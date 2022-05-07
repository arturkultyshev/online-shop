from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
import os
from flask_msearch import Search
from flask_login import LoginManager
from dotenv import load_dotenv


app = Flask(__name__)
load_dotenv()
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
search = Search()
search.init_app(app)

# запрашивает местоположение файла(адрес), в котором выполняется код
BASEDIR = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = f'{os.getenv("SQLALCHEMY_URI")}'
app.config['SECRET_KEY'] = f'{os.getenv("SECRET_K")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = f'{os.getenv("SQLALCHEMY_TRACK_MOD")}'
app.config['UPLOADED_PHOTOS_DEST'] = f'{os.getenv("UPLOADED_PHOTOS_D")}'


photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view ='customerLogin'
login_manager.needs_refresh_message_category='danger'
login_manager.login_message = u"Please login first"


from e_shop.products import routes
from e_shop.admin import routes
from e_shop.busket import busket
from e_shop.users import routes

