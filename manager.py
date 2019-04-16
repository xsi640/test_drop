# coding: utf-8
'''
author: suyang
'''
from app import create_app

__author__ = 'suyang'

app = create_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=app.config['PORT'])
