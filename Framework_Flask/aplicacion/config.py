import os

SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
PWD = os.path.abspath(os.curdir)

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://juanjo:juanjosecano7@juanjo.mysql.pythonanywhere-services.com/juanjo$AnalisisTwitter'
SQLALCHEMY_TRACK_MODIFICATIONS = False