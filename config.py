import os
import urllib.parse 
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'hello22.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'hello-wolrd22-db'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'udacityadmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'Password@123'
    # SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'

    params = urllib.parse.quote_plus("DRIVER={SQL Server};SERVER=hello22.database.windows.net;DATABASE=hello-wolrd22-db;UID=udacityadmin;PWD=Password@123")
    SQLALCHEMY_DATABASE_URI = "mssql+pyodbc:///?odbc_connect=%s" % params

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'hellostorage22'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'ea+CS200pfMazMP1o8YHpiZ8fTZV4bx83Ss96ygduuI+DYaNBHvf0LAYgxaB6FpzsZ2GB4aWyEMY+AStU3Lkug=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'
