"""
create by khan.hozin 2020/7/2
"""
__author__ = 'hozin'

DEBUG=True
SECRET_KEY="547bef953e0941759b144c83385876b8"
SQLALCHEMY_TRACK_MODIFICATIONS=False
#数据库用户名
DB_USERNAME='root'
#数据库密码
DB_PASSWORD="Aa123.com"
#数据库主机
DB_HOST="202.182.110.99"
#数据库端口
DB_PORT="31789"
#数据库名
DB_NAME="sport_data"
DB_URI='mysql+cymysql://%s:%s@%s:%s/%s'%(DB_USERNAME,DB_PASSWORD,DB_HOST,DB_PORT,DB_NAME)
SQLALCHEMY_DATABASE_URI=DB_URI
WTF_CSRF_ENABLED = False
ADMIN_USER_ID='_2jF67s#k7a3N0*(z(@%_Y'