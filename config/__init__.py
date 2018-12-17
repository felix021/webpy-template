#coding:utf-8

import os

from . import dev, production

_env = os.getenv('WEBPYENV', 'dev')

config = {
    'dev': dev.config,
    'production': production.config,
}

def isProduction():
    return _env == 'production'

def Read(key, default=None):
    return config[_env].get(key, default)

def dsn(db):
    return 'mysql://%s:%s@%s:%s/%s' % (
        Read(db)['user'],
        Read(db)['pass'],
        Read(db)['host'],
        Read(db)['port'],
        Read(db)['name']
    )
