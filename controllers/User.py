#coding:utf-8

import web
import random
import string

from models.User import User

class init:
    def GET(self):
        from models import Base, engine
        users_table = User.__table__
        metadata = Base.metadata
        metadata.create_all(engine)
        return 'OK\n'

class add:
    def GET(self):
        web.header('Content-type', 'text/html')
        fname = "".join(random.choice(string.letters) for i in range(4))
        lname = "".join(random.choice(string.letters) for i in range(7))
        u = User(name=fname, fullname=fname + ' ' + lname, password=542)
        web.ctx.orm.add(u)
        web.ctx.orm.commit()
        return "added:" + web.websafe(str(u)) \
                + "<br/>" \
                + '<a href="/view">view all</a>'

class view:
    def GET(self):
        web.header('Content-type', 'text/plain')
        session = web.ctx.orm

        users = session.query(User).filter_by(id=1)
        return "\n".join(map(str, users.all()))

