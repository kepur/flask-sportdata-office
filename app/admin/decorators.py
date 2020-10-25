"""
create by khan.hozin 2020/7/5
"""
__author__ = 'hozin'
from flask import session,redirect,url_for
from functools import wraps
import config
def login_required(func):
    #传给wrap函数保留func的属性
    @wraps(func)
    def inner(*args,**kwargs):
        if config.ADMIN_USER_ID in session:
            return func(*args,**kwargs)
        else:
            return redirect(url_for('admin.login'))
    return inner