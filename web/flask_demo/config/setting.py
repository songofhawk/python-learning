# SQLALCHEMY_ECHO = True

PROPAGATE_EXCEPTIONS = True
SQLALCHEMY_DATABASE_URI = 'mysql://root:viabtcpool_1@localhost/python_learning'

SITE_URL = "http://localhost"

import pymysql
pymysql.install_as_MySQLdb()
