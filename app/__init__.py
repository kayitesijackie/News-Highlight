from flask import Flask
from flask_bootstrap import Bootstrap
from .config import DevConfig

app = Flask(__name__,instance_relative_config = True)
bootstrap = Bootstrap(app)

app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

from app import views

# def create_app(config_name):

#     app = Flask(__name__)

#     # Creating the app configurations
#     app.config.from_object(config_options[config_name])

#     #Initializing flask extensions
#     bootstrap.init_app(app)

#     # Registering the blueprint
#     from .main import main as main_blueprint
#     app.register_blueprint(main_blueprint)

#     # setting config
#     from .requests import configure_request
#     configure_request(app)

#     # Will add the views
#     return app
