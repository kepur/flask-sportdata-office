"""
create by khan.hozin 2020/7/7
"""
__author__ = 'hozin'

from wtforms import Form

class BaseForm(Form):
    def get_error(self):
        message=self.errors.popitem()[1][0]
        return message