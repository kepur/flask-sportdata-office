"""
create by khan.hozin 2020/7/5
"""
__author__ = 'hozin'

from app.admin import admin
from app import db
from flask import render_template, views, request, session, redirect, url_for,jsonify
from .forms import LoginForm,ResetpwdForm
from .models import AdminUser
from .decorators import login_required
import config
from flask import g
from app.utils import restful

@admin.route('/')
@login_required
def index():
    return render_template('admin/cms_index.html')

@admin.route('/logout/')
def logout():
    del session[config.ADMIN_USER_ID]
    return redirect(url_for('admin.login'))

@admin.route('/profile')
@login_required
def profile():
    return render_template('admin/cms_profile.html')


@admin.route('/boards')
@login_required
def boards():
    return render_template('admin/cms_boards.html')

class LoginView(views.MethodView):
    def get(self,message=None):
        return render_template('admin/cms_login.html',message=message)

    def post(self):
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            remember = form.remember.data
            user = AdminUser.query.filter_by(email=email).first()
            if user and user.check_password(password):
                session[config.ADMIN_USER_ID]=user.id
                if remember:
                    #如果设置session.permanent=True 过期时间是31天
                    session.permanent=True
                return redirect(url_for('admin.index'))
            else:
                return self.get(message="邮箱或密码错误")
        else:
            message=form.get_error()
            print(message)
            return self.get(message=message)

class ResetPwdView(views.MethodView):
    decorators=[login_required]
    def get(self):
        return render_template('admin/cms_resetpwd.html')
    def post(self):
        form=ResetpwdForm(request.form)
        if form.validate():
            oldpwd=form.oldpwd.data
            newpwd=form.newpwd.data
            user=g.admin_user
            if user.check_password(oldpwd):
                user.password=newpwd
                db.session.commit()
                #{code:400}
                # return jsonify({'code':200,"messgae":""})
                # return restful.resuful_result(200,message="",data=None)
                return restful.success()
            else:
                # return jsonify({"code":400,"message":"旧密码错误"})
                return restful.params_error("旧密码错误")

        else:
            message=form.get_error()
            # return jsonify({"code":400,"message":message})
            return restful.params_error(message)


@admin.before_request
def before_req():
    if config.ADMIN_USER_ID in session:
        user_id=session.get(config.ADMIN_USER_ID)
        user=AdminUser.query.get(user_id)
        if user:
            g.admin_user = user



admin.add_url_rule('/login/',view_func=LoginView.as_view('login'))
admin.add_url_rule('/resetpwd/',view_func=ResetPwdView.as_view("resetpwd"))