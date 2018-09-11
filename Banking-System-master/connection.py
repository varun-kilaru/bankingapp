__author__ = 'user'

import cx_Oracle



con = cx_Oracle.connect("system","pvpsit","localhost/xe")
cur = con.cursor()
