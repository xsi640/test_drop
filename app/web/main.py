# coding: utf-8
'''
author: suyang
'''
from flask import render_template
from . import web

__author__ = 'suyang'


@web.route("/")
def main():
    return render_template("login.html")
