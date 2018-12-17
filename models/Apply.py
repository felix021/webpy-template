#coding:utf-8

from . import *

class Apply(Base):
    __tablename__ = 'apply'
    id = Column(Integer, primary_key=True)
    apply_no = Column(String(32), unique=True)
    status = Column(Integer)

    STATUS_NEW      = 1
    STATUS_AUDITING = 2
    STATUS_PASSED   = 3
    STATUS_LOADEN   = 4
    STATUS_REPAID   = 5

    def __init__(self, apply_no, status=STATUS_NEW):
        self.apply_no = apply_no
        self.status = status

    def __repr__(self):
        return "<Apply(%d, '%s')>" % (self.id, self.apply_no)
