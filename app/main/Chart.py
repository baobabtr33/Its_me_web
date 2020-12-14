from matplotlib import pyplot as plt
import matplotlib.font_manager as fm
import re
import math
import pandas as pd
import numpy as np
from scipy.stats import norm


from matplotlib import font_manager
font_manager._rebuild()
for i in font_manager.fontManager.ttflist:
    if 'Nanum' in i.name:
        print(i.name, i.fname) 

def Credit_Rating(point):
    rv = norm(loc=650, scale=300)
    if (point <= rv.ppf(0.99999)) & (point >= rv.ppf(0.95)):
        y = '1'
    elif (point <= rv.ppf(0.95)) & (point >= rv.ppf(0.85)):
        y = '2'
    elif (point <= rv.ppf(0.85)) & (point >= rv.ppf(0.7)):
        y = '3'
    elif (point <= rv.ppf(0.7)) & (point >= rv.ppf(0.5)):
        y = '4'
    elif (point <= rv.ppf(0.5)) & (point >= rv.ppf(0.3)):
        y = '5'
    elif (point <= rv.ppf(0.3)) & (point >= rv.ppf(0.15)):
        y = '6'
    elif (point <= rv.ppf(0.15)) & (point >= rv.ppf(0.05)):
        y = '7'
    elif (point <= rv.ppf(0.05)) & (point >= rv.ppf(0.00001)):
        y = '8'
    return y

def Calculate_Rest_Point(point):
    level = Credit_Rating(point)
    rv = norm(loc = 650, scale = 300)
    if level == '1':
        y = 0
    elif level == '2':
        y= rv.ppf(0.95) - point
    elif level == '3':
        y= rv.ppf(0.85) - point
    elif level == '4':
        y= rv.ppf(0.7)- point
    elif level == '5':
        y= rv.ppf(0.5)- point
    elif level == '6':
        y= rv.ppf(0.3)- point
    elif level == '7':
        y= rv.ppf(0.15)- point
    elif level == '8':
        y= rv.ppf(0.05)- point
    return int(y)



def Draw_Distribution(username, point):

    plt.style.use('default')
    plt.rcParams['figure.figsize'] = (6, 3)
    plt.rcParams['axes.unicode_minus'] = False
    plt.rcParams['font.size'] = 12
    plt.rcParams['font.family'] = 'NanumGothic'
    plt.rcParams['lines.linewidth'] = 5


    rv = norm(loc=650, scale=300)
    x = np.arange(0, 1800, 1)
    y = rv.pdf(x)
    fig, ax = plt.subplots(1, 1)
    
    plt.plot(x,y,alpha=0.7,label=r"이츠미 사용자 분포")
    plt.xlabel("It's Me 포인트")
    plt.ylabel("사용자 누적 비율")
    plt.title("{}님의 신용분포".format(username))
    # TODO : 한글 깨짐

    # 사용자 위치 표시
    percent = rv.cdf(point)  # 퍼센트 구하기
    score = rv.ppf(percent)  # 퍼센트 x값 구하기
    x_score = np.arange(score, x.max() + 1, 1)  # range 만들기
    y_score = rv.pdf(x_score)  # 범위에 따른 확률값 구하기
    
    ax.vlines(x_score, 0,  y_score, colors='steelblue', lw = 5,  label= "{}님 현재 위치".format(username))
    plt.legend(bbox_to_anchor=(0.65, 0.95), fontsize= 8)

    plt.legend(bbox_to_anchor=(0.65, 0.95), fontsize=8)

    file_save = "./app/static/img/dist/" + username + '-dist.jpg'
    plt.savefig(file_save, bbox_inches='tight')
    plt.clf()

    return file_save


def create_x(t, w, n, d):
    return [t * x + w * n for x in range(d)]


def Draw_BarChart(username, user_df):

    plt.style.use('default')
    plt.rcParams['figure.figsize'] = (6, 3)
    plt.rcParams['axes.unicode_minus'] = False
    plt.rcParams['font.family'] = 'NanumGothic'
    plt.rcParams['font.size'] = 10
    plt.rcParams['lines.linewidth'] = 5

    topics = ['종합(%)', '과제제출(%)', '출석(%)']
    avg = [89.28, 88.51, 90.05]
    user = user_df
    avg_x = create_x(2, 0.8, 1, 3)
    user_x = create_x(2, 0.8, 2, 3)

    ax = plt.subplot()
    ax.bar(avg_x, avg, facecolor='#9999ff', edgecolor='white')
    ax.bar(user_x, user, facecolor='#ff9999', edgecolor='white')

    for x, y in zip(avg_x, avg):
        plt.text(x - 0.01, y + 4.5, '{}%'.format(y), ha='center', va='top', fontsize=7.5)

    for x, y in zip(user_x, user):
        plt.text(x + 0.01, y + 4.5, '{}%'.format(y), ha='center', va='top', fontsize=7.5)

    middle_x = [(a + b) / 2 for (a, b) in zip(avg_x, user_x)]
    ax.set_xticks(middle_x)
    ax.set_xticklabels(topics)

    plt.xlabel('평가기준')
    plt.ylabel('퍼센트(%)')
    plt.legend(['평균', username], loc='upper center', bbox_to_anchor=(0.85, 0.25), ncol=1, fontsize=9)

    plt.title("{}님의 학교생활 데이터".format(username))

    file_save = "./app/static/img/barchart/" + username + '-barchart.jpg'
    plt.savefig(file_save, bbox_inches='tight')
    plt.clf()

    return file_save
