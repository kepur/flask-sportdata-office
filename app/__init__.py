"""
create by khan.hozin 2020.07.02
"""
__author__ = 'hozin'
from app.models import db
from flask import Flask
def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    register_blueprint(app)
    db.init_app(app)
    with app.app_context():
        db.create_all(app=app)
    return app

def register_blueprint(app):
    from app.home import home as home_bp
    app.register_blueprint(home_bp,url_prefix='/')


sport_index=create_app()


