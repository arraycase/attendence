
import logging
import os
from flask import Flask, request, current_app
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_cors import CORS
from flask_marshmallow import Marshmallow
# import sentry_sdk
# from sentry_sdk.integrations.flask import FlaskIntegration
# from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity

db = SQLAlchemy()
ma = Marshmallow()
cors = CORS()

# jwt = JWTManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    # jwt.init_app(app)
    ma.init_app(app)
    cors.init_app(app)

    # sentry_sdk.init(
    #     dsn="https://3313de1a38b04d3ea4ec37ea3f7ad81b@sentry.io/1759344",
    #     integrations=[FlaskIntegration()]
    # )
    with app.app_context():
        
        from app.employee import bp as employee_bp
        app.register_blueprint(employee_bp, url_prefix='/employee')

     
        db.create_all()

        # from app.model import Role
        # if Role(name="ADMIN").query.first():
        #     pass
        # else:

        #     db.session.add(Role(name='ADMIN'))
        #     db.session.commit()
    return app