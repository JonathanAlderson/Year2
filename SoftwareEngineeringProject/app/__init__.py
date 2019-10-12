from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin #import for the flask admin page
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

#admin
admin = Admin(app,template_mode='bootstrap3')


migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
@login_manager.user_loader
def load_user(user_id):
    return None
login_manager.login_view='login'
login_manager.login_message_category='info'

mail = Mail(app)


from app import views, models
