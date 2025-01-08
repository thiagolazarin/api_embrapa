from flask import Flask
from flask_caching import Cache
from flasgger import Swagger
from flask_httpauth import HTTPBasicAuth

# Initialize the Flask app
app = Flask(__name__)
app.config.from_object('app.config.Config')

# Initialize extensions
cache = Cache(app)
auth = HTTPBasicAuth()

# Configure Swagger
swagger = Swagger(app)

from app.utils import auth as auth_utils

from app.routes import scrape_routes