from flask_restless import APIManager

from app import app, db
from app.main_module.models import YouModel

manager = APIManager(app, flask_sqlalchemy_db = db)
manager.create_api(YouModel, methods=['GET'])
