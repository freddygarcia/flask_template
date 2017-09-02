from flask import Flask
# from flask_httpauth import HTTPBasicAuth
# from flask_login import LoginManager
# from flask_sqlalchemy import SQLAlchemy

# App Instance
app = Flask(__name__)

# Configuration
app.config.from_object('config')

# Http Auth Instance
# auth = HTTPBasicAuth()

# Login manager instance
# login_manager = LoginManager()

# db instance
# db = SQLAlchemy(app)

# login manager (duh!)
# login_manager.init_app(app)

# registre routes
from app.main_module.routes import routes

# registre routes auth
# from app.main_module.routes import auth_routes

# registre apis
# from app.main_module import api

# administration
# from app.main_module.admin import admin

# authentication
# from app.main_module import auth

# populate db
# from app.main_module import populate_db

