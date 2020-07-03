"""
create by khan.hozin 2020/7/2
"""
__author__ = 'hozin'


from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()
from datetime import datetime


#插入日期
class Football_Math_Date_Data(db.Model):
    __tablename__='math_date'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    date_name=db.Column(db.String(200),nullable=False)
    football_matchs=db.relationship("Football_MATCH",backref="math_date",lazy='dynamic',cascade='all,delete-orphan',passive_deletes=True)
    #添加时间
    add_time=db.Column(db.DateTime,index=True,default=datetime.now())

#比赛相关数据
class Football_MATCH(db.Model):
    __tablename__='football_match'

    football_match_id=db.Column(db.Integer,primary_key=True)
    # 简称
    LEAGUE_NAME_SIMPLY= db.Column(db.String(100),nullable=True)

    #比赛日期
    LEAGUE_DATA=db.Column(db.String(100),nullable=True)
    #主队名
    H0ST_TEAM_NAME=db.Column(db.String(200))
    #比晒时间
    MATCH_TIME=db.Column(db.String(100),nullable=True)
    #客队名字
    GUEST_TEAM_NAME=db.Column(db.String(100),nullable=True)
    #主队得分
    HOST_TEAM_GOAL=db.Column(db.Integer,nullable=True)
    #客队得分
    GUEST_TEAM_GOAL=db.Column(db.Integer,nullable=True)
    #添加时间
    add_time=db.Column(db.DateTime,index=True,default=datetime.now())

    #盘点日期
    match_time_id=db.Column(db.Integer,db.ForeignKey('math_date.id',ondelete='CASCADE'))
    #公司
    companys=db.relationship("Companys",backref="football_match",lazy='dynamic',cascade='all, delete',passive_deletes=True)


class Companys(db.Model):
    __tablename__='sports_companys'
    company_id=db.Column(db.Integer,primary_key=True)
    #公司
    COMPANY_NAME=db.Column(db.String(100))
    #主队
    HOST=db.Column(db.Float)
    #让球
    HANDICAP=db.Column(db.Float)
    #客队
    GUEST=db.Column(db.Float)
    #主胜
    WIN=db.Column(db.Float)
    #和局
    SAME=db.Column(db.Float)
    #客胜
    LOST=db.Column(db.Float)
    #大球
    BIG=db.Column(db.Float)
    #盘口
    DW_HANDICAP=db.Column(db.Float)
    #小球
    SMALL=db.Column(db.Float)

    #主队
    FIRST_HOST=db.Column(db.Float)
    #让球
    DW_FIRST_HANDICAP=(db.Float)
    #客队
    FIRST_GUEST=db.Column(db.Float)
    #主胜
    FIRST_WIN=db.Column(db.Float)
    #客胜
    FIRST_LOST=db.Column(db.Float)
    #小球
    FIRST_SMALL=db.Column(db.Float)
    #大球
    FIRST_BIG=db.Column(db.Float)
    #和局
    FIRST_SAME=db.Column(db.Float)
    #添加时间
    add_time=db.Column(db.DateTime,index=True,default=datetime.now())
    match_id=db.Column(db.Integer,db.ForeignKey('football_match.football_match_id',ondelete='CASCADE'),)



