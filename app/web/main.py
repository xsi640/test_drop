# coding: utf-8
'''
author: suyang
'''
from flask import render_template
from flask_login import login_required

from . import web

__author__ = 'suyang'


@web.route("/")
@login_required
def main():
    return render_template("index.html")
