"""
create by khan.hozin 2020/7/2
"""
__author__ = 'hozin'


from flask import Blueprint

home=Blueprint('home',__name__)

from app.models import Football_Math_Date_Data,Football_MATCH,Companys
from flask import render_template
import datetime

@home.route('/')
def index():
    # datetime_now = str(datetime.datetime.now().strftime('%Y-%m-%d'))
    # today=Football_Math_Date_Data.query.filter(Football_Math_Date_Data.date_name.like(datetime_now)).first()
    # if today is not None:
    #     football_match=Football_MATCH.query.filter(Football_MATCH.match_time_id==today.id).all()
    # else:
    #     football_match=Football_MATCH.query.all()
    # companys=Companys.query.all()
    # return render_template('index.html',football_matchs=football_match,companys=companys)
    return render_template('index.html')

#文章列表
@home.route('/blog-list')
def blog_list():
    return render_template('blog-list.html')

#文章详情
@home.route('/blog-detail')
def blog_detail():
    return render_template('blog-detail.html')

#球队详情专家推荐
@home.route('/teamdetails')
def team_details():
    return render_template('team-details.html')

#球队比晒时间
@home.route('/team-schedule')
def team_schedule():
    return render_template('team-schedule.html')

#即将来到
@home.route('/comingsoon')
def commingsoon():
    return render_template('comingsoon.html')


@home.route('/knowledge')
def knowledge():
    return render_template('knowledge.html')

def getYesterday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=2)
    yesterday = today - oneday
    return yesterday.strftime('%Y-%m-%d')

@home.route('/record',methods=['GET'])
def record(datetime=getYesterday()):
    # all_data=Football_Math_Date_Data.query.all()
    yuesterday=Football_Math_Date_Data.query.filter(Football_Math_Date_Data.date_name.like(datetime)).first()
    football_match=Football_MATCH.query.filter(Football_MATCH.match_time_id==yuesterday.id).all()
    companys=Companys.query.all()
    return render_template('record.html',football_matchs=football_match,companys=companys)

#
@home.route('/info')
def info():
    football_match=Football_MATCH.query.filter(Football_MATCH.match_time_id).all()
    return render_template("info.html",football_matchs=football_match)


@home.route('/iframe')
def iframe():
    datetime_now = str(datetime.datetime.now().strftime('%Y-%m-%d'))
    today=Football_Math_Date_Data.query.filter(Football_Math_Date_Data.date_name.like(datetime_now)).first()
    football_match=Football_MATCH.query.filter(Football_MATCH.match_time_id==today.id).all()
    companys=Companys.query.all()
    return render_template('index_iframe.html',football_matchs=football_match,companys=companys)

@home.route('/history',methods=['GET'])
def history_iframe(datetime=getYesterday()):
    yuesterday=Football_Math_Date_Data.query.filter(Football_Math_Date_Data.date_name.like(datetime)).first()
    football_match=Football_MATCH.query.filter(Football_MATCH.match_time_id==yuesterday.id).all()
    companys=Companys.query.all()
    return render_template('history_iframe.html',football_matchs=football_match,companys=companys)

#全局
@home.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@home.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'),500

