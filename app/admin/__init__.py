"""
create by khan.hozin 2020/7/5
"""
__author__ = 'hozin'

from flask import Blueprint
admin=Blueprint('admin',__name__)
import app.admin.views