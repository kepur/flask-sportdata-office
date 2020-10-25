"""
create by khan.hozin 2020/7/5
"""
__author__ = 'hozin'

from wtforms import StringField,BooleanField
from wtforms.validators import Email,InputRequired,Length,EqualTo
from app.forms import BaseForm



class LoginForm(BaseForm):
    email = StringField(validators=[Email(message='请输入正确的邮箱格式'),InputRequired(message='请输入邮箱')])
    password=StringField(validators=[Length(6,20,message="请输入正确格式的密码")])
    remember=BooleanField('记住我')


class ResetpwdForm(BaseForm):
    oldpwd=StringField(validators=[Length(6,20,message='请输入正确格式的旧密码')])
    newpwd=StringField(validators=[Length(6,20,message='请输入正确格式的新密码')])
    newpwd2=StringField(validators=[EqualTo("newpwd",message="确认密码必须和新密码保持一致")])