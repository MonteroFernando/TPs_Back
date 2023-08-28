from flask import Flask
from config import Config
from .routes.product_bp import product_bp

def inicializar_app():
    app=Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(product_bp)
    return app
