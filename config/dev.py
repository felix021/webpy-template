#coding:utf-8

import logging

config = {
    'db': {
        'host': '127.0.0.1',
        'port': '3306',
        'user': 'root',
        'pass': '123456',
        'name': 'test'
    },
    'log': {
        'type': 'file',
        'path': 'runtime/log/app.log',
    },
}

#用本地配置覆盖
try:
    from . import local
    for k, v in local.config.items():
        config[k] = v
except:
    pass
