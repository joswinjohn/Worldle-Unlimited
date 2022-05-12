from flask import Flask
import json
from locations.country import Country
from flask import session
from flask_session import Session
from config import Config
from views import worldle
import os


class App:
  def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
      SECRET_KEY='dev',
    )

    app.register_blueprint(worldle.bp)
    
    @app.route('/')
    def index():
      return 'bad'
    
    app.run(host='0.0.0.0', port=81)
  create_app()
