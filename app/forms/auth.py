# coding: utf-8
'''
author: suyang
'''
from wtforms import Form, StringField, PasswordField, ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo

from app.models.user import User

__author__ = 'suyang'


class RegisterForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64), Email(message='电子邮件不合法')])
    password = PasswordField(validators=[DataRequired(message='密码不能为空'), Length(6, 32)])
    nickname = StringField(validators=[DataRequired(), Length(2, 10, message='昵称至少两个字符')])

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('电子邮件已被注册')

    def validate_nickname(self, field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('昵称已被注册')


class EmailForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64), Email(message='电子邮件不合法')])


class LoginForm(EmailForm):
    password = PasswordField(validators=[DataRequired(message='密码不能为空'), Length(6, 32)])


class ResetPasswordForm(Form):
    password1 = PasswordField(validators=[
        DataRequired(),
        Length(6, 32, message='密码长度6~32'),
        EqualTo('password2', message='两次密码输入不同')
    ])
    password2 = PasswordField(validators=[
        DataRequired(),
        Length(6, 32)
    ])
