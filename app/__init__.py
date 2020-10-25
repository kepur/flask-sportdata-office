"""
create by khan.hozin 2020.07.02
"""
__author__ = 'hozin'
from app.models import db
from flask import Flask
from flask_wtf import CSRFProtect
from flask_login import LoginManager
login_manager=LoginManager()
login_manager.login_view ='admin.login'


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    login_manager.init_app(app)
    register_blueprint(app)
    CSRFProtect(app)
    db.init_app(app)
    with app.app_context():
        db.create_all(app=app)
    return app

def register_blueprint(app):
    from app.home import home as home_bp
    from app.admin import admin as admin_bp
    app.register_blueprint(home_bp,url_prefix='/')
    app.register_blueprint(admin_bp,url_prefix='/admin')

sport_index=create_app()


@login_manager.user_loader
def user_loader(user_id):
    from app.admin.models import AdminUser
    return AdminUser.query.get(int(user_id))
