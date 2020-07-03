#coding:utf-8
"""
create by khan.hozin 2020/7/2
"""
__author__ = 'hozin'

USER_AGENTS = [
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
	"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
	"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
	"Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
	"Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
	"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
	"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
	"Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
	"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
	"Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
	"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
	"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
	"Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
	"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
	"Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52"
]

#连接数据库
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import config
engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
Base = declarative_base()
Session=sessionmaker(bind=engine)
sport_session = Session()

import requests,json
import datetime

#获取当前日期
DateTimeNow = str(datetime.datetime.now().strftime('%Y-%m-%d'))
def getYesterday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    return yesterday.strftime('%Y-%m-%d')

#获取网站数据
def get_football_data(load_time=DateTimeNow):
	url='http://odds.zgzcw.com/odds/oyzs_ajax.action'
	import random
	headers={
		'User-Agent':random.choice(USER_AGENTS)
	}
	Params_Data={
		"type":"jc",
		"companys":"3,12,4,23,14,8,17,31,22,9",
        "issue":load_time
	}
	resp=requests.get(url,headers=headers,params=Params_Data)
	result=json.loads(resp.text)
	return result

from app.models import Football_Math_Date_Data, Football_MATCH, Companys


#插入时间
def insert_datatime(datetime=DateTimeNow):
    datatime_in_db=sport_session.query(Football_Math_Date_Data.date_name).filter(Football_Math_Date_Data.date_name.like(datetime)).first()
    if  datatime_in_db is None:
        time_data=Football_Math_Date_Data()
        time_data.date_name=datetime
        sport_session.add(time_data)
        sport_session.commit()
    footballmathdate=sport_session.query(Football_Math_Date_Data.id).filter(Football_Math_Date_Data.date_name == datetime).first()
    return footballmathdate.id


def Insert_save_db(date_id,data):
    last_one=sport_session.query(Football_MATCH.football_match_id).order_by(Football_MATCH.football_match_id.desc()).first()
    if last_one:
        i=int(last_one.football_match_id+1)
    else:
        i=1
    for mathinfo in data:
        fotballmath = Football_MATCH()
        fotballmath.football_match_id=i
        fotballmath.LEAGUE_NAME_SIMPLY=mathinfo['LEAGUE_NAME_SIMPLY']
        fotballmath.LEAGUE_DATA=mathinfo['CC_ID']
        fotballmath.H0ST_TEAM_NAME=mathinfo['HOST_NAME']
        fotballmath.MATCH_TIME=mathinfo['MATCH_TIME']
        fotballmath.GUEST_TEAM_NAME=mathinfo['GUEST_NAME']

        try:
            if mathinfo['HOST_GOAL'] and mathinfo['HOST_GOAL'] !=0:
                fotballmath.HOST_TEAM_GOAL = mathinfo['HOST_GOAL']
                print("主场得分:{}".format(mathinfo['HOST_GOAL']))
            elif mathinfo['HOST_GOAL'] == 0 :
                fotballmath.HOST_TEAM_GOAL = 0

        except:
            print("没有主场队分数")
        try:
            if mathinfo['GUEST_GOAL'] and mathinfo['GUEST_GOAL']!= 0:
                fotballmath.GUEST_TEAM_GOAL = mathinfo['GUEST_GOAL']
                print("客场得分:{}".format(mathinfo['GUEST_GOAL']))
            elif mathinfo['GUEST_GOAL'] == 0 :
                fotballmath.GUEST_TEAM_GOAL = 0

        except:
            print("没有客场队分数")
        fotballmath.match_time_id=date_id
        try:
            sport_session.add(fotballmath)
            sport_session.commit()
        except:
            print("主键重复")

        if mathinfo['listOdds']:
            company_last_one = sport_session.query(Companys.company_id).order_by(
                Companys.company_id.desc()).first()
            if company_last_one:
                n=company_last_one.company_id+1
            else:
                n=1
            for listodd in mathinfo['listOdds']:
                companys = Companys()
                companys.company_id=n
                if listodd['COMPANY_NAME']:
                    companys.COMPANY_NAME=listodd['COMPANY_NAME']
                try:
                    if listodd['HOST']:
                        companys.HOST=float(listodd['HOST'])
                except:
                    print("没有主名")
                try:
                    if listodd['HANDICAP']:
                        companys.HANDICAP=float(listodd['HANDICAP'])
                except:
                    print("没有 HANDICAP东西")

                try:
                    if listodd['GUEST']:
                        companys.GUEST = float(listodd['GUEST'])
                except:
                    print("没有 GUEST")
                try:
                    if listodd['HANDICAP']:
                        companys.WIN = float(listodd['WIN'])
                except:
                    print('没有 HANDICAP')
                try:
                    if listodd['SAME']:
                        companys.SAME = float(listodd['SAME'])
                except:
                    print("没有 HANDICAP")
                try:
                    if listodd['LOST']:
                        companys.LOST = float(listodd['LOST'])
                except:
                    print("没有 LOST")
                try:
                    if listodd['BIG']:
                        companys.BIG = float(listodd['BIG'])
                except:
                    print("没有 BIG")
                try:
                    if listodd['DW_HANDICAP']:
                        companys.DW_HANDICAP = float(listodd['DW_HANDICAP'])
                except:
                    print("没有 DW_HANDICAP")
                try:
                    if listodd['SMALL']:
                        companys.SMALL = float(listodd['SMALL'])
                except:
                    print("没有 SMALL")
                try:
                    if listodd['FIRST_HOST']:
                        companys.FIRST_HOST = float(listodd['FIRST_HOST'])
                except:
                    print("没有 FIRST_HOST")
                try:
                    if listodd['DW_FIRST_HANDICAP']:
                        companys.DW_FIRST_HANDICAP = float(listodd['DW_FIRST_HANDICAP'])
                except:
                    print("没有 DW_FIRST_HANDICAP")

                try:
                    if listodd['FIRST_GUEST']:
                        companys.FIRST_GUEST = float(listodd['FIRST_GUEST'])
                except:
                    print("没有 FIRST_GUEST")

                try:
                    if listodd['FIRST_WIN']:
                        companys.FIRST_WIN = float(listodd['FIRST_WIN'])
                except:
                    print("没有 FIRST_WIN")

                try:
                    if listodd['FIRST_LOST']:
                        companys.FIRST_LOST = float(listodd['FIRST_LOST'])
                except:
                    print("没有 FIRST_LOST")

                try:
                    if listodd['FIRST_SMALL']:
                        companys.FIRST_SMALL = float(listodd['FIRST_SMALL'])
                except:
                    print("没有 FIRST_SMALL")

                try:
                    if listodd['FIRST_BIG']:
                        companys.FIRST_BIG = float(listodd['FIRST_BIG'])
                except:
                    print("没有 FIRST_BIG")
                try:
                    if listodd['FIRST_SAME']:
                        companys.FIRST_SAME = float(listodd['FIRST_SAME'])
                except:
                    print("没有 FIRST_SAME")


                companys.match_id=i
                n+=1
                try:
                    sport_session.add(companys)
                    sport_session.commit()
                except:
                    print("添加公司失败")
        i+=1

def get_data_insert_in_db(datetime):
    #提交当前的日志
    id=insert_datatime(datetime)
    #获取主球信息
    data=get_football_data(datetime)
    print(data)
    #保存到数据库
    Insert_save_db(id,data)

def delete_datetime_in_db(datetime):
    datetime_data=sport_session.query(Football_Math_Date_Data).filter(Football_Math_Date_Data.date_name.like(datetime)).first()
    try:
        sport_session.delete(datetime_data)
        sport_session.commit()
        print("删除成功")
        return True
    except:
        print("删除失败")
        return False




if __name__ == '__main__':

    #指定获取某个固定时间段数据
    # dateTime = '2020-07-02'
    # get_data_insert_in_db(dateTime)

    #指定获取某个固定时间段数据
    # dateTime = '2020-07-02'
    # get_data_insert_in_db(dateTime)

    get_data_insert_in_db(DateTimeNow)
    #删除昨天重新抓取昨日数据
    try:
        yusterday=getYesterday()
        get_data_insert_in_db(yusterday)
        print("昨天日期为:{}".format(yusterday))
        delete_datetime_in_db(yusterday)
        get_data_insert_in_db(yusterday)
        import time
        time.sleep(1)
        print("更新昨日赛程记录成功")
    except:
        print("更新昨日赛程记录失败")
    try:
        get_data_insert_in_db(DateTimeNow)
        print("更新今日数据成功")
    except:
        print("更新今日数据失败")





