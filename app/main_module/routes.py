from flask import Blueprint, redirect, jsonify, request, render_template, url_for, flash, g, session
from app import app
	
routes = Blueprint('routes', __name__, url_prefix='/')

@routes.route("")
def works():
	return 'It works!'

app.register_blueprint(routes)
