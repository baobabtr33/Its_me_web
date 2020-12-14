# file name : index.py
# pwd : /project_name/app/main/index.py
from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as current_app
from .NHmrobo_API import NH_API
from .NHmrobo_API import DB
from . import Chart
import random
import datetime
from scipy.stats import norm

main = Blueprint('main', __name__, url_prefix='/')

@main.route('/main', methods = ['GET'])
def index():
    return render_template('/main/index.html')


# decorating index function with the app.route with url as /login
@main.route('/main/login', methods = ['GET'])
def login():
   return render_template('/main/login.html')


@main.route("/assignments", methods=['POST',"GET"])
def baskin():
    if request.method == "POST":
        if "Addpoint" in request.form:
            NH_API.check(itsme_info, user_info)
    return render_template("main/attendance2.html")


@main.route("/attendance", methods=['POST',"GET"])
def user():
    if request.method == "POST":
        if "Addpoint" in request.form:
            NH_API.check(itsme_info, user_info)
    return render_template("main/attendance.html")


@main.route('/success',  methods=['POST'])
def success():
   if request.method == 'POST':
       Name = request.form['Name']
       # It's Me 계좌에서 가지고 올 값
       Point = '12'
       Monthly_Point = len(a.get_trade_ids("000751", 20201211160000))
       # 출석 페이지, 과제 페이지에서 가져올 값
       Attendance  = '100'
       Assignment = '94.85'
       Total = '97.43'
       # 최종 누계 포인트와 신용 등급 값
       Total_Point = 800
       user_df = [97.43, 94.85, 100.0]
       # 일단 안씀
       Chart.Draw_Distribution(Name, Total_Point)
       Chart.Draw_BarChart(Name, user_df)

       # 퍼센트 계산
       rv = norm(loc = 650, scale = 300)
       percent = round(100 - rv.cdf(Total_Point) * 100, 2)

       # 신용등급 계산
       Credit_Rate = Chart.Credit_Rating(Total_Point)
       # 나머지 점수 계산
       rest = Chart.Calculate_Rest_Point(Total_Point)

       return render_template('/main/success.html', Name=Name, Point = Point, Monthly_Point =Monthly_Point ,Attendance = Attendance,
                              Assignment = Assignment, Total = Total, Total_Point = Total_Point, percent= percent, Credit_Rate = Credit_Rate,
                              rest = rest)
   else:
       pass



# decorating index function with the app.route with url as /login
@main.route('/main/point', methods = ['GET'])
def point():
   return render_template('/main/point.html')


@main.route('/pointsuccess',  methods=['POST'])
def pointsuccess():
   if request.method == 'POST':
       Name = request.form['Name']
       Point = len(a.get_trade_ids("000751", 20201211160000))
       return render_template('/main/pointsuccess.html', Name=Name, Point = Point)
   else:
       pass


a = DB.DBBot("NH")
a.get_connection()

# itsme_infos
AccessToken = "79f94971b3be510a39f475a10e5e0ccd8a096c4316c04c12b9cbce0c0dfc7f7a"
Iscd = "000704"  # 기업코드
Tsymd = datetime.datetime.now().strftime("%Y%m%d") # 오늘 날짜
BrdtBrno = "19501211" # 생년월일
Bncd = "011"
Acno = "3020000003001"
FinAcno = "00820100007040000000000005724"
random_sequence = "".join([str(i) for i in list(random.sample([0,1,2,3,4,5,6,7,8,9], 9))])

itsme_info = {"AccessToken" : AccessToken, 'Iscd' : Iscd, "BrdtBrno" : BrdtBrno, "Bncd" : Bncd, "Acno" : Acno, "FinAcno" : FinAcno }


# user_infos
AccessToken = "51904849dc027093a8ed3072e4a7389b3b30da24fe3225be2527d8f14258d05b"
Iscd = "000751"  # 기업코드
Tsymd = datetime.datetime.now().strftime("%Y%m%d")  # 오늘 날짜
BrdtBrno = "19501213"  # 생년월일
Bncd = "011"
Acno = "3020000003229"
FinAcno = "00820100007510000000000005759"
random_sequence = "".join([str(i) for i in list(random.sample([0,1,2,3,4,5,6,7,8,9], 9))])

user_info = {"AccessToken" : AccessToken, 'Iscd' : Iscd, "BrdtBrno" : BrdtBrno, "Bncd" : Bncd, "Acno" : Acno, "FinAcno" : FinAcno }

