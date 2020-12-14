import requests
import json
from requests.auth import HTTPBasicAuth
import datetime
import random
import pandas as pd
import uuid
import psycopg2
from . import DB
import shortuuid


# itsme_infos
AccessToken = "79f94971b3be510a39f475a10e5e0ccd8a096c4316c04c12b9cbce0c0dfc7f7a"
#기업코드
Iscd = "000704"
#오늘 날짜
Tsymd = datetime.datetime.now().strftime("%Y%m%d")
#생년월일
BrdtBrno = "19501211"
Bncd = "011"
Acno = "3020000003001"
FinAcno = "00820100007040000000000005724"
random_sequence = "".join([str(i) for i in list(random.sample([0,1,2,3,4,5,6,7,8,9], 9))])

itsme_info = {"AccessToken" : AccessToken, 'Iscd' : Iscd, "BrdtBrno" : BrdtBrno, "Bncd" : Bncd, "Acno" : Acno, "FinAcno" : FinAcno }





# user_infos
AccessToken = "51904849dc027093a8ed3072e4a7389b3b30da24fe3225be2527d8f14258d05b"
#기업코드
Iscd = "000751"
#오늘 날짜
Tsymd = datetime.datetime.now().strftime("%Y%m%d")
#생년월일
BrdtBrno = "19501213"
Bncd = "011"
Acno = "3020000003229"
FinAcno = "00820100007510000000000005759"
random_sequence = "".join([str(i) for i in list(random.sample([0,1,2,3,4,5,6,7,8,9], 9))])

user_info = {"AccessToken" : AccessToken, 'Iscd' : Iscd, "BrdtBrno" : BrdtBrno, "Bncd" : Bncd, "Acno" : Acno, "FinAcno" : FinAcno }







def withdrawl(user, amount, message = ""):

    url_items = "https://developers.nonghyup.com/DrawingTransfer.nh"
    headers = {'Content-type':'application/json', 'Accept':'application/json'}


    AccessToken = user['AccessToken']
    #기업코드
    Iscd = user['Iscd']
    #생년월일
    BrdtBrno = user['BrdtBrno']
    Bncd = user['Bncd']
    Acno = user["Acno"]
    FinAcno = user["FinAcno"]

    Tsymd = datetime.datetime.now().strftime("%Y%m%d")
    Trtm = datetime.datetime.now().strftime("%H%M%S")
    IsTuno = "".join([str(i) for i in list(random.sample([0,1,2,3,4,5,6,7,8,9], 9))])


    newItem = {"Header": {
        "ApiNm": "DrawingTransfer",
        "Tsymd": Tsymd,
        "Trtm": Trtm,
        "Iscd": Iscd,
        "FintechApsno": "001",
        "ApiSvcCd": "DrawingTransferA",
        "IsTuno": IsTuno,
        "AccessToken": AccessToken
          },
  "FinAcno": FinAcno,
  "Tram": amount,
  "DractOtlt": "test",
  "MractOtlt":"테스트"

}

    r = requests.post(url_items, auth=HTTPBasicAuth('shany.ka', 'shanky1213'), json=newItem, headers=headers)

    r_text= json.loads(r.text)

    if '정상' in r_text['Header']['Rsms'] :
        return {'uuid': shortuuid.uuid(), 'trade_time' : int(Tsymd+Trtm)}
    else :
        raise ValueError(str(r_text['Header']['Rsms']))







def deposit(user, amount, message = "university_attendance"):

    url_items = "https://developers.nonghyup.com/ReceivedTransferAccountNumber.nh"
    headers = {'Content-type':'application/json', 'Accept':'application/json'}

    AccessToken = user['AccessToken']
    #기업코드
    Iscd = user['Iscd']
    #생년월일
    BrdtBrno = user['BrdtBrno']
    Bncd = user['Bncd']
    Acno = user["Acno"]

    Tsymd = datetime.datetime.now().strftime("%Y%m%d")
    IsTuno = "".join([str(i) for i in list(random.sample([0,1,2,3,4,5,6,7,8,9], 9))])
    Trtm = datetime.datetime.now().strftime("%H%M%S")

    newItem = {
      "Header": {
        "ApiNm": "ReceivedTransferAccountNumber",
        "Tsymd":Tsymd,
        "Trtm":Trtm,
        "Iscd": Iscd,
        "FintechApsno":"001",
        "ApiSvcCd":"ReceivedTransferA",
        "IsTuno": IsTuno,
        "AccessToken": AccessToken
            },
      "Bncd": "011",
      "Acno": Acno,
      "Tram": amount,
      "DractOtlt": message,
      "MractOtlt": message
    }

    r = requests.post(url_items, auth=HTTPBasicAuth('shany.ka', 'shanky1213'), json=newItem, headers=headers)

    r_text= json.loads(r.text)
    print(r.text)
    print(r.status_code)
    print(r_text)







def check_trades(user, start_time =''):
    headers = {'Content-type':'application/json', 'Accept':'application/json'}
    url_items = "https://developers.nonghyup.com/InquireTransactionHistory.nh"


    AccessToken = user['AccessToken']
    #기업코드
    Iscd = user['Iscd']
    #생년월일
    BrdtBrno = user['BrdtBrno']
    Bncd = user['Bncd']
    Acno = user["Acno"]

    Tsymd = datetime.datetime.now().strftime("%Y%m%d")
    IsTuno = "".join([str(i) for i in list(random.sample([0,1,2,3,4,5,6,7,8,9], 9))])
    Trtm = datetime.datetime.now().strftime("%H%M%S")

    newItem = {
    "Header":{
        "ApiNm":"InquireTransactionHistory",
        "Tsymd":Tsymd,
        "Trtm":Trtm,
        "Iscd": Iscd,
        "FintechApsno":"001",
        "ApiSvcCd":"ReceivedTransferA",
        "IsTuno":IsTuno,
        "AccessToken":
        AccessToken},
        "Bncd":Bncd,
        "Acno":Acno,
        "Insymd":"20201201",
        "Ineymd":Tsymd,
        "TrnsDsnc":"A",
        "Lnsq":"DESC",
        "PageNo":"1",
        "Dmcnt":"100"
    }


    r = requests.post(url_items, auth=HTTPBasicAuth('shany.ka', 'shanky1213'), json=newItem, headers=headers)
    r_text= json.loads(r.text)
#     print(r.status_code)

#     print(r_text)
    a = pd.DataFrame(r_text['REC'])
    a['trade_time'] = a['Trdd'] + a['Txtm']
    a['trade_time'] = a['trade_time'].map(int)
    a.sort_values(by=['Trdd', 'Txtm'], axis=0, inplace=True, ascending = False)
    if start_time != '':
        a = a[a['trade_time']>= start_time]
    return a





def check_balance(user):
    headers = {'Content-type':'application/json', 'Accept':'application/json'}
    url_items = "https://developers.nonghyup.com/InquireBalance.nh"


    AccessToken = user['AccessToken']
    #기업코드
    Iscd = user['Iscd']
    #생년월일
    BrdtBrno = user['BrdtBrno']
    Bncd = user['Bncd']
    Acno = user["Acno"]
    FinAcno = user["FinAcno"]

    Tsymd = datetime.datetime.now().strftime("%Y%m%d")
    IsTuno = "".join([str(i) for i in list(random.sample([0,1,2,3,4,5,6,7,8,9], 9))])

    newItem = {
        "Header": {
            "ApiNm": "InquireBalance",
            "Tsymd": Tsymd,
            "Trtm": "112428",
            "Iscd": Iscd,
            "FintechApsno": "001",
            "ApiSvcCd": "ReceivedTransferA",
            "IsTuno": IsTuno,
            "AccessToken": AccessToken
        },
        "FinAcno": FinAcno
    }

    r = requests.post(url_items, auth=HTTPBasicAuth('shany.ka', 'shanky1213'), json=newItem, headers=headers)
    r_text= json.loads(r.text)
    print(r.status_code)
    print(r_text)
    return r_text['Ldbl']





def check(itsme_info, user_info):
    a = DB.DBBot("NH")
    trade = withdrawl(itsme_info, 1)
    trade_id = trade['uuid']
    trade_time = trade['trade_time']
    deposit(user_info, 1, trade_id)
    user_balance = check_balance(user_info)
    a.insert_order(trade_id,user_info['Iscd'], trade_time)
    print(trade_time)
    return user_balance




# print(withdrawl(itsme_info, 1))
# print(deposit(user_info, 1))
# print(check_trades(user_info, 20201213160000))
# print(check_balance(user_info))
# print(check(itsme_info, user_info))

# a = DB.DBBot("NH")
# print(a.get_connection())
# print(a.get_trade_ids("000751", 20201211160000))
