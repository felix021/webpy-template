#coding:utf-8

import web
import random
import string
from libraries import log

# /test/hello-world
class HelloWorld:
    def GET(self):
        log.debug("this is a test")
        return "this is a test\n"
