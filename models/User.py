#coding:utf-8

from . import *

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    fullname = Column(String(64))
    password = Column(String(32))

    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password

    def __repr__(self):
        return "<User(%d, '%s','%s', '%s')>" % (self.id, self.name, self.fullname, self.password)
