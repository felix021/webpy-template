#coding:utf-8

import web
import random
import string

from libraries import log

from . import ResponseJson

from models.Apply import Apply

class add:
    def GET(self):
        a = Apply(apply_no='20181218%06d' % random.randint(0, 100000))
        web.ctx.orm.add(a)
        web.ctx.orm.commit()

        log.debug("added: " + str(a))

        return ResponseJson(0, 'added: ' + str(a))
