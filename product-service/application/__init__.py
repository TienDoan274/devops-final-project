# application/__init__.py
import config
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from prometheus_flask_exporter import PrometheusMetrics

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    metrics = PrometheusMetrics(app)

    metrics.info(f'product_info', f'product API info', version='1.0.0')
    environment_configuration = os.environ['CONFIGURATION_SETUP']
    app.config.from_object(environment_configuration)

    db.init_app(app)

    with app.app_context():
        from .product_api import product_api_blueprint
        app.register_blueprint(product_api_blueprint)
        return app
