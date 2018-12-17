#coding:utf-8

import os
import re
import glob
import inspect
import importlib

urls = []

def CamelToDash(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1-\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1-\2', s1).lower()

for filename in glob.glob('controllers/*.py'):
    filename = os.path.basename(filename)[:-3]
    if filename == '__init__':
        continue

    package = importlib.import_module('controllers.' + filename)
    for clsname, cls in inspect.getmembers(package, inspect.isclass):
        if not callable(getattr(cls, 'GET', None)) and not callable(getattr(cls, 'POST', None)):
            continue
        
        url = getattr(cls, 'url', None)
        if not url:
            url = '/%s/%s' % (CamelToDash(filename), CamelToDash(clsname))
 
        urls.append(url)
        urls.append(cls)
