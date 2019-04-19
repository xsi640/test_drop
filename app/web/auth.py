from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user

from app.forms.auth import RegisterForm, LoginForm, EmailForm, ResetPasswordForm
from app.libs.email import send_mail
from app.models.user import User
from . import web

__author__ = 'suyang'


@web.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.find_user(form.username.data)
        if user and user.check_password(form.password.data):
            login_user(user)
            next = request.args.get('next')
            if not next or not next.startswith('/'):
                next = url_for('web.main')
            return redirect(next)
        else:
            flash('账号不存在或密码错误')
    return render_template('login.html', form=form)


@web.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('web.login'))


@web.route("/initUser")
def initUser():
    user = User()
    user.username = 'admin'
    user.password = 'admin123'
    user.save()
    return "add user."
