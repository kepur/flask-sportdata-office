"""
create by khan.hozin 2020/7/2
"""
__author__ = 'hozin'

from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
from app.models import *
from app import sport_index
from app.admin import models as admin_models

ADMINUser=admin_models.AdminUser
# CMSRole=admin_models.CMSRole
# CMSPermission=admin_models.CMSPersmission

manager=Manager(sport_index)

magrate = Migrate(sport_index,db)

manager.add_command('db',MigrateCommand)


@manager.option('-u','--username',dest='username')
@manager.option('-p','--password',dest='password')
@manager.option('-m','--mail',dest='mail')
def add_admin_user(username,mail,password):
    user = ADMINUser(username=username,usermail=mail,password=password,)
    db.session.add(user)
    db.session.commit()
    print('cms用户添加成功！')


# @manager.command
# def create_role():
#     #访问者
#     # 1. 访问者（可以修改个人信息）
#     visitor = CMSRole(name='访问者',desc='只能相关数据，不能修改。')
#     visitor.permissions = CMSPermission.VISITOR
#
#     # 2. 运营角色（修改个人个人信息，管理帖子，管理评论，管理前台用户）
#     operator = CMSRole(name='运营',desc='管理帖子，管理评论,管理前台用户。')
#     operator.permissions = CMSPermission.VISITOR|CMSPermission.POSTER|CMSPermission.CMSUSER|CMSPermission.COMMENTER|CMSPermission.FRONTUSER
#
#     # 3. 管理员（拥有绝大部分权限）
#     admin = CMSRole(name='管理员',desc='拥有本系统所有权限。')
#     admin.permissions = CMSPermission.VISITOR|CMSPermission.POSTER|CMSPermission.CMSUSER|CMSPermission.COMMENTER|CMSPermission.FRONTUSER|CMSPermission.BOARDER
#
#     # 4. 开发者
#     developer = CMSRole(name='开发者',desc='开发人员专用角色。')
#     developer.permissions = CMSPermission.ALL_PERMISSION
#
#     db.session.add_all([visitor,operator,admin,developer])
#     db.session.commit()
#
# @manager.command
# def test_permission():
#     user = ADMINUser.query.first()
#     if user.is_developer:
#         print('这个用户有访问者的权限！')
#     else:
#         print('这个用户没有访问者权限！')
#
#
# @manager.option('-e','--email',dest='email')
# @manager.option('-n','--name',dest='name')
# def add_user_to_role(email,name):
#     user = ADMINUser.query.filter_by(email=email).first()
#     if user:
#         role = CMSRole.query.filter_by(name=name).first()
#         if role:
#             role.users.append(user)
#             db.session.commit()
#             print('用户添加到角色成功！')
#         else:
#             print('没有这个角色：%s'%role)
#     else:
#         print('%s邮箱没有这个用户!'%email)
#
#
# @manager.command
# def init_databases():
#     db.drop_all()
#     db.create_all()

if __name__ == '__main__':
    manager.run()