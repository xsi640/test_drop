# coding: utf-8
'''
author: suyang
'''
from flask import Flask
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate, Manager, MigrateCommand

import config
from app import setting
from app.models.base import db

__author__ = 'suyang'

login_manager = LoginManager()
mail = Mail()


def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    app.config.from_object(setting)

    register_blueprint(app)

    login_manager.init_app(app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先登录或注册'

    mail.init_app(app)

    migrate = Migrate(app, db)
    db.init_app(app)
    db.create_all(app=app)

    return app
