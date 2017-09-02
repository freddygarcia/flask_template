from app.main_module.models import YourModel

# Administration Site
class CustomModelView(ModelView):
	pass

class RestaurantModelView(CustomModelView):
	column_list = ('name', 'category', 'thumbnail')
	form_excluded_columns = ['lat', 'lng', 'rating']
	column_labels = dict(name='Nombre', category='Categoria', thumbnail='Miniatura')

	def prefix_name(obj, file_data):
	    parts = os_path.splitext(file_data.filename)
	    return secure_filename('file-%s%s' % parts)

	form_extra_fields = {
		'thumbnail' : form.ImageUploadField('Miniatura',
										base_path=app.config['UPLOAD_IMG_FOLDER'],
										namegen=prefix_name,
										thumbnail_size=(100,100, True))
	}


	def _list_thumbnail(view, contet, model, name):
		if not model.thumbnail:
			return Markup('<img width=28 src="/static/default.ico" />')

		return Markup('<img width=28  src="%s" />' %  url_for('static',filename=form.thumbgen_filename(model.thumbnail)))

	column_formatters = {
		'thumbnail' : _list_thumbnail
	}

# Create customized index view class that handles login & registration
class MyAdminIndexView(AdminIndexView):

	@expose('/')
	def index(self):
		if not current_user.is_authenticated:
			return redirect(url_for('login'))
	# @expose('/login/', methods=('GET', 'POST'))
	# def login_view(self):
	#     # handle user login
	#     form = LoginForm(request.form)
	#     if helpers.validate_form_on_submit(form):
	#         user = form.get_user()
	#         login_user(user)

	#     if current_user.is_authenticated:
	#         return redirect(url_for('.index'))
	#     link = '<p>Don\'t have an account? <a href="' + url_for('.register_view') + '">Click here to register.</a></p>'
	#     self._template_args['form'] = form
	#     self._template_args['link'] = link
	#     return super(MyAdminIndexView, self).index()

	# @expose('/register/', methods=('GET', 'POST'))
	# def register_view(self):
	#     form = RegistrationForm(request.form)
	#     if helpers.validate_form_on_submit(form):
	#         user = User()

	#         form.populate_obj(user)
	#         # we hash the users password to avoid saving it as plaintext in the db,
	#         # remove to use plain text:
	#         user.password = generate_password_hash(form.password.data)

	#         db.session.add(user)
	#         db.session.commit()

	#         login_user(user)
	#         return redirect(url_for('.index'))
	#     link = '<p>Already have an account? <a href="' + url_for('.login_view') + '">Click here to log in.</a></p>'
	#     self._template_args['form'] = form
	#     self._template_args['link'] = link
	#     return super(MyAdminIndexView, self).index()

	# @expose('/logout/')
	# def logout_view(self):
	#     logout_user()
	#     return redirect(url_for('.index'))


admin = Admin(app, name='Top Restaurants', template_mode='bootstrap3', index_view=MyAdminIndexView())
admin.add_view(RestaurantModelView(Restaurant, db.session, 'Restaurantes'))
admin.add_link(MenuLink(name='Cerrar Sesion', url='/logout'))


