#coding:utf-8

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

import config
engine = create_engine(config.dsn('db'), echo=not config.isProduction())
