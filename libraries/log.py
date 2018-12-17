#coding:utf-8

import logging
import config

fmt   ='[%(asctime)s][%(levelname)s][%(name)s][%(pathname)s:%(lineno)d] %(message)s'
level = logging.INFO if config.isProduction() else logging.DEBUG

log_config = config.Read('log')
if log_config['type'] == 'file':
    logging.basicConfig(filename=log_config['path'], level=level, format=fmt)
else:
    raise Exception("unsupported log type: " + log_config['type'])

from logging import debug, info, warning, error, critical
