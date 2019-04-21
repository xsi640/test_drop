# coding: utf-8
'''
author: suyang
'''
from sqlalchemy import Column, Integer, String, func

from app.models.base import Base, db

__author__ = 'suyang'


class Menu(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    description = Column(String(50), nullable=True)
    layer = Column(Integer, nullable=False)
    parent_id = Column(Integer, nullable=False)

    def save(self):
        parent = Menu.query.filter_by(id=self.parent_id).first()
        self.layer = parent.layer + 1
        with db.auto_commit():
            db.session.add(self)

    @staticmethod
    def find_children(parent_id):
        Menu.query.filter_by(parent_id=int(parent_id)).all()

    @staticmethod
    def count_children(parent_id):
        Menu.query(func.count(Menu.id).filter(Menu.parent_id == int(parent_id))).scalar()
