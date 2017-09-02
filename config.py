from os import path

# Enable Development enviroment
Debug = True

# Application directory
BASE_DIR = path.abspath(path.dirname(__file__))

# Database config
DB_CONFIG = {
    'PROTOCOL': '', # 'mysql+pymysql',
    'HOST': '', #'127.0.0.1',
    'USER': '', #'root',
    'PASS': '', #'root',
    'PORT': '', #'3306',
    'DB': '' 
}

SQLALCHEMY_DATABASE_URI = "{PROTOCOL}://{USER}:{PASS}@{HOST}/{DB}".format(**DB_CONFIG)
SQLALCHEMY_TRACK_MODIFICATIONS = False
DATABASE_CONNECT_OPTIONS = {}

# Flask-Security config
SECURITY_URL_PREFIX = "/admin"
SECURITY_PASSWORD_HASH = "pbkdf2_sha512"
SECURITY_PASSWORD_SALT = "ATGUOHAELKiubahiughaerGOJAEGj"

# Flask-Security URLs, overridden because they don't put a / at the end
# SECURITY_LOGIN_URL = "/login/"
# SECURITY_LOGOUT_URL = "/logout/"
# SECURITY_REGISTER_URL = "/register/"

# SECURITY_POST_LOGIN_VIEW = "/admin/"
# SECURITY_POST_LOGOUT_VIEW = "/admin/"
# SECURITY_POST_REGISTER_VIEW = "/admin/"

# Flask-Security features
SECURITY_REGISTERABLE = True
SECURITY_SEND_REGISTER_EMAIL = False
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Session key
SECRET_KEY = 'secret'