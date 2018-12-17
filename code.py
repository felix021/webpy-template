#coding:utf-8

import web
from route import urls
from libraries import log

from sqlalchemy.orm import scoped_session, sessionmaker
from models import engine

def load_sqlalchemy(handler):
    web.ctx.orm = scoped_session(sessionmaker(bind=engine))
    return handler() #no auto commit

    # if auto commit is desired, uncomment following lines:
    #try:
    #    return handler()
    #except web.HTTPError:
    #   web.ctx.orm.commit()
    #   raise
    #except:
    #    web.ctx.orm.rollback()
    #    raise
    #finally:
    #    web.ctx.orm.commit()

app = web.application(urls, globals())
app.add_processor(load_sqlalchemy)

if __name__ == "__main__":
    app.run()
