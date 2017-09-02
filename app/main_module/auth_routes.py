from flask import Blueprint, redirect, jsonify, request, render_template, url_for, flash, g
import flask_login

from app import app, login_manager, auth
from app.main_module.models import User

routes = Blueprint('auth_routes', __name__, url_prefix='/')

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'GET':
		return render_template('authentication/login.html')

	email = request.form['email']
	passw = request.form['password']
	user = User.query.filter_by(email=email).first()

	if user:
		if user.verify_password(passw):
			flask_login.login_user(user)
			return redirect('/admin')
		else:
			flash('Password invalido', 'login_error')
	else:
		flash('Usuario no encontrado', 'login_error')

	return render_template('authentication/login.html')


@app.route('/api/token', methods=['GET', 'POST'])
@auth.login_required
def get_auth_token():
	token = g.user.generate_auth_token()
	return jsonify(token=token.decode('ascii'))


@app.route('/api')
@auth.login_required
def it_works():
	return 'It works!'

@auth.verify_password
def verify_password(username_or_token, password):
    user = User.verify_auth_token(username_or_token)

    if not user:
        user = User.query.filter_by(username = username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True

@app.route('/protected')
@flask_login.login_required
def protected():
	return 'Logged in as: ' + str(flask_login.current_user.id)


@app.route('/logout')
def logout():
	flask_login.logout_user()
	return redirect(url_for('login'))


@login_manager.unauthorized_handler
def unauthorized_handler():
	return 'Unauthorized'

app.register_blueprint(routes)
