#coding:utf-8

import web

from . import ResponseJson

# 使用 url 字段替换默认路径 /site/index
class Index:
    url = '/'
    def GET(self):
        return "Hello, world!\n"

# 默认路径 /site/login
class Login:
    def POST(self):
        #do something
        return ResponseJson(0)
