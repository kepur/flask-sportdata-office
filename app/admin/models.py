"""
create by khan.hozin 2020/7/5
"""
__author__ = 'hozin'

from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from app import db,login_manager

class CMSPersmission(object):
    # 255的二进制方式来表示 1111 1111
    ALL_PERMISSION = 0b11111111
    # 1. 访问者权限
    VISITOR =        0b00000001
    # 2. 管理帖子权限
    POSTER =         0b00000010
    # 3. 管理评论的权限
    COMMENTER =      0b00000100
    # 4. 管理板块的权限
    BOARDER =        0b00001000
    # 5. 管理前台用户的权限
    FRONTUSER =      0b00010000
    # 6. 管理后台用户的权限
    CMSUSER =        0b00100000
    # 7. 管理后台管理员的权限
    ADMINER =        0b01000000

cms_role_user = db.Table(
    'cms_role_user',
    db.Column('cms_role_id',db.Integer,db.ForeignKey('cms_role.id'),primary_key=True),
    db.Column('cms_user_id',db.Integer,db.ForeignKey('admin_user.id'),primary_key=True)
)


class CMSRole(db.Model):
    __tablename__ = 'cms_role'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    desc = db.Column(db.String(200),nullable=True)
    create_time = db.Column(db.DateTime,default=datetime.now)
    permissions = db.Column(db.Integer,default=CMSPersmission.VISITOR)
    users = db.relationship('AdminUser',secondary=cms_role_user,backref='roles')

#用户名
class AdminUser(db.Model):
    __tablename__ = 'admin_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80),nullable=False,unique=True)
    usermail = db.Column(db.String(200),nullable=False,unique=True)
    _password=db.Column(db.String(128),nullable=False)
    addtime=db.Column(db.DateTime,default=datetime.now)

    def __init__(self,username,password):
        self.password=password
        self.username=username

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self,raw_pasword):
        self._password=generate_password_hash(raw_pasword)

    def check_password(self,raw_password):
        #按照原来的方法进行加密 查看是否一致
        result = check_password_hash(self.password,raw_password)
        return result

    @property
    def permissions(self):
        if not self.roles:
            return 0
        all_permissions = 0
        for role in self.roles:
            permissions = role.permissions
            all_permissions |= permissions
        return all_permissions

    def has_permission(self,permission):
        # all_permissions = self.permissions
        # result = all_permissions&permission == permission
        # return result
        return self.permissions&permission == permission

    @property
    def is_developer(self):
        return self.has_permission(CMSPersmission.ALL_PERMISSION)