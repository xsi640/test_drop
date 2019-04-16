# coding: utf-8
'''
author: suyang
'''
from flask import Blueprint, render_template

__author__ = 'suyang'

web = Blueprint('web', __name__)


@web.app_errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404


from . import auth
from . import main
