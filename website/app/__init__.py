from flask import Flask
from app.routes.cloud import weather_bp

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')
    app.register_blueprint(weather_bp)  # DO NOT use url_prefix here
    return app
