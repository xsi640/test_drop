# coding: utf-8
'''
author: suyang
'''
from wtforms import Form, StringField
from wtforms.validators import DataRequired, Length, ValidationError

from app.models.menu import Menu

__author__ = 'suyang'


class MenuForm(Form):
    name = StringField(validators=[DataRequired(message='菜单名称不能为空'), Length(2, 20)])

    def validate_parent_id(self, field):
        if Menu.parent_id != 0 and Menu.count_children(field.data) == 0:
            raise ValidationError('请选择存在的父菜单')
