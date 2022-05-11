from flask import Flask
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
    app.config['SESSION_PERMANENT'] = False
    app.config['SESSION_TYPE'] = 'filesystem'
    Session(app)

    app.register_blueprint(worldle.bp)
    
    @app.route('/')
    def index():
      return '<p>Hello from Flask!<p>'
    
    app.run(host='0.0.0.0', port=81)
  create_app()
