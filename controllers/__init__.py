#coding:utf-8

import web
try:
    import simplejson as json
except:
    import json

def ResponseJson(code, message='', data={}):
    web.header('Content-Type','application/json; charset=utf-8', unique=True) 
    return json.dumps({'code': code, 'message': message, 'data': data}, ensure_ascii=False) + "\n"
