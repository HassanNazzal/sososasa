import json
import requests
import time
import hashlib
import urllib.parse
import os
import urllib3
import linecache
import sys
import shutil
import base64
from bs4 import BeautifulSoup as s
import string
import os
import pymongo
import re
import random
import timeit
import urllib.parse as urlparse
from urllib.parse import parse_qs
from datetime import timedelta
import datetime
from requests_toolbelt.multipart.encoder import MultipartEncoder
import random, string

# point users
client2user = pymongo.MongoClient("mongodb+srv://aa:bb@cluster0.579gc.mongodb.net/?retryWrites=true&w=majority")
mydb = client2user["aww"]

mycol = mydb["users"]
allgive = "1000000"
list = [""]
payload = {}
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
    'Cookie': "_gcl_au=1.1.1356179306.1654897263; _clck=1cgd6aj|1|f27|0; _fbp=fb.1.1654897268650.1976387684; _uetsid=07912190e90611ec850d3f7e4f1bc9ba; _uetvid=07914980e90611ec80439bb33468a5dc; _ga=GA1.2.1521470733.1654897281; _gid=GA1.2.1445687506.1654897281; _gat_UA-20169249-1=1; G_ENABLED_IDPS=google; _tt_enable_cookie=1; _ttp=fe015226-26fb-48eb-8871-ef8f5644a1f0; _hjSessionUser_1400488=eyJpZCI6IjJhMGE4ZmVjLTNkMTItNTk1Ni05ODY5LThiOWEzNjgzZTM2MCIsImNyZWF0ZWQiOjE2NTQ4OTcyODg3NzAsImV4aXN0aW5nIjpmYWxzZX0=; _hjFirstSeen=1; _hjIncludedInSessionSample=1; _hjSession_1400488=eyJpZCI6IjdjNmQxMmNlLWY2OWYtNGZhMC1iYmViLTU2MzFhNTY0YjY2MyIsImNyZWF0ZWQiOjE2NTQ4OTcyODg4MjIsImluU2FtcGxlIjp0cnVlfQ==; _hjIncludedInPageviewSample=1; _hjAbsoluteSessionInProgress=0; accessToken=d29887aca4ff1324f3eddf88733d3488dac721f9; refreshToken=33849ae2ea410aa32fc9e3b2f237bbced6bf266b; bartlebyRefreshTokenExpiresAt=2022-07-10T21:42:27.203Z; userId=403cf126-1c9b-486c-b65f-15e272d90e47; userStatus=A1; promotionId=; sku=bb1499_plus; _hjCachedUserAttributes=eyJhdHRyaWJ1dGVzIjp7ImNvdW50cnkiOiJJUSIsImdlb2dyYXBoeSI6IkludGVybmF0aW9uYWwiLCJzdWJzY3JpcHRpb25fbW9udGgiOiIiLCJ1c2VyX3NvdXJjZSI6IkNPTVBBU1MiLCJ1c2VyX3N0YXR1cyI6IkExIn0sInVzZXJJZCI6IjQwM2NmMTI2LTFjOWItNDg2Yy1iNjVmLTE1ZTI3MmQ5MGU0NyJ9; btbHomeDashboardAnimationTriggerDate=2022-06-11T21:42:32.575Z; btbHomeDashboardTooltipAnimationCount=1; _gat_UA-93748-2=1; ki_r=; ABTasty=uid=8ah0v2ex6d20gwg3&fst=1654897269513&pst=-1&cst=1654897269513&ns=1&pvt=6&pvis=6&th=831945.1034156.1.1.1.1.1654897402185.1654897402185.1; ABTastySession=mrasn=&sen=5&lp=https%3A%2F%2Fwww.bartleby.com%2Flogin; _clsk=hba32t|1654897402260|5|0|b.clarity.ms/collect; ki_t=1654897354337;1654897354337;1654897402829;1;4; endCycleWhenQuestionsRemainingWasClosed=2022-06-15T07:00:00.000Z; OptanonConsent=isGpcEnabled=0&datestamp=Sat+Jun+11+2022+00:43:31+GMT+0300+(Arabian+Standard+Time)&version=6.32.0&isIABGlobal=false&hosts=&consentId=fb6b4871-7ad0-4716-9cce-05fcb50dc1a2&interactionCount=1&landingPath=NotLandingPage&groups=C0001:1,C0003:1,BG142:1,C0002:1,C0005:1,C0004:1&AwaitingReconsent=false; _hjUserAttributesHash=bf5bcc710ce7db51e46109d319983a5b"
}
TOKEN = "5509372745:AAEWrZZlB4kISr2h-j5bBJD8rtOxmxaP9nY"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)

hh1 = '''  <html>
                                                                                                             <head> 
                                                                                                            <meta charset="utf-8"/>        
                                                                                                             <meta name="viewport" content="width=device-width, initial-scale=1.0" /> 
                                                                                                                    </head>
                                                                                                                            <body      '''

hh2 = '''</body>
                                                     </html>   '''


class ParseMode(object):
    MARKDOWN = 'Markdown'
    MARKDOWN_V2 = 'MarkdownV2'
    HTML = 'HTML'


def get_url(url):
    try:
        response = requests.get(url)
        content = response.content.decode("utf-8")
        return (content)
    except:
        pass


def post_url(urll, data, file=None):
    try:
        if file is not None:
            response = requests.post(urll, files=file, data=data)
            return json.loads(response.content.decode())
        else:
            response = requests.post(urll, data=data)
            return json.loads(response.content.decode())
    except:
        pass


def get_updates(offset=None):
    try:
        url = URL + "getUpdates?timeout=100"
        if offset:
            url += "&offset={}".format(offset)
        content = get_url(url)
        js = json.loads(content)
        return js
    except:
        pass


def get_last_update_id(updates):
    try:
        update_ids = []
        for update in updates["result"]:
            update_ids.append(int(update["update_id"]))
        return max(update_ids)
    except:
        pass


def zro(repy_id):
    try:
        mydoc2 = mycol.find_one({str(repy_id): str(repy_id)})
        print(mydoc2)
        print("is sub grube")
        g = [mydoc2]
        oldadd = int(g[0]['point'])
        newadd = int(g[0]['point'])
        clc = oldadd - newadd
        print("is clc sub  :" + str(clc))
        mydict77 = {str(repy_id): str(repy_id), "point": str(clc)}
        mydict4 = {"$set": mydict77}
        mycol.update_one(mydoc2, mydict4)
        return str(clc)
    except:
        pass


# sub grupe
def sub_point(user_id):
    try:
        mydoc2 = mycol.find_one({str(user_id): str(user_id)})
        print(mydoc2)
        print("is sub ")
        g = [mydoc2]
        oldadd = int(g[0]['point'])
        newadd = int("1")
        clc = oldadd - newadd
        print("is clc sub  :" + str(clc))
        mydict77 = {str(user_id): str(user_id), "point": str(clc)}
        mydict4 = {"$set": mydict77}
        mycol.update_one(mydoc2, mydict4)
        return str(clc)
    except:
        pass


# sub num all
def all4subb(add):
    try:
        j = []
        mydoc2 = mycol.find()
        for x in mydoc2:
            g = [x]
            j.append(g)
        for ch in j:
            print(ch[0])
            oldadd = int(ch[0]['point'])
            newadd = int(add)
            clc = oldadd - newadd
            print("is clc :" + str(clc))
            print(ch[0]['_id'])
            myy = {"point": str(ch[0]['point'])}
            mydict77 = {"point": str(clc)}
            mydict4 = {"$set": mydict77}
            mycol.update_one(ch[0], mydict4)
    except:
        pass


# add all points

def all4add(add):
    try:
        j = []
        mydoc2 = mycol.find()
        for x in mydoc2:
            g = [x]
            j.append(g)
        for ch in j:
            print(ch[0])
            oldadd = int(ch[0]['point'])
            newadd = int(add)
            clc = oldadd + newadd
            print("is clc :" + str(clc))
            print(ch[0]['_id'])
            myy = {"point": str(ch[0]['point'])}
            mydict77 = {"point": str(clc)}
            mydict4 = {"$set": mydict77}
            mycol.update_one(ch[0], mydict4)
    except:
        pass


# sub all points

def all4sub(add):
    try:
        j = []
        mydoc2 = mycol.find()
        for x in mydoc2:
            g = [x]
            j.append(g)
        for ch in j:
            print(ch[0])
            oldadd = int(ch[0]['point'])
            newadd = int("0")
            clc = oldadd * newadd
            print("is clc :" + str(clc))
            print(ch[0]['_id'])
            myy = {"point": str(ch[0]['point'])}
            mydict77 = {"point": str(clc)}
            mydict4 = {"$set": mydict77}
            mycol.update_one(ch[0], mydict4)
    except:
        pass


# add points
def add_point(repy_id, add):
    try:
        # print("id group points :"+str(chat_id)+"and add point :"+str(add_point))
        mydoc2 = mycol.find_one({str(repy_id): str(repy_id)})
        print(mydoc2)
        if str(repy_id) not in str(mydoc2):
            mydict = {str(repy_id): str(repy_id), "point": str(add)}
            x = mycol.insert_one(mydict)
            return str(add)
        else:
            print("is old grupe")
            g = [mydoc2]
            oldadd = int(g[0]['point'])
            newadd = int(add)
            clc = oldadd + newadd
            print("is clc :" + str(clc))
            mydict77 = {str(repy_id): str(repy_id), "point": str(clc)}
            mydict4 = {"$set": mydict77}
            mycol.update_one(mydoc2, mydict4)
            return str(clc)
    except:
        pass


# chuck point
def get_point(user_id):
    try:
        print("id  points :" + str(user_id))
        mydoc2 = mycol.find_one({str(user_id): str(user_id)})
        print(mydoc2)
        if str(user_id) not in str(mydoc2):
            mydict = {str(user_id): str(user_id), "point": allgive}
            x = mycol.insert_one(mydict)
            return allgive
        else:
            g = [mydoc2]
            print("user is old in file time :" + str(g[0]['point']))
            return str(g[0]['point'])
    except:
        pass


def Check(update):
    try:
        if not 'callback_query' in str(update) and not 'channel_post' in str(update):

            user_id = update["message"]["from"]["id"]
            chat_id = update["message"]["chat"]["id"]
            chat_type = update["message"]["chat"]["type"]
            message_text = update['message']['text']
            try:
                first_name = update["message"]["from"]["first_name"]
            except:
                first_name = ''
            try:
                last_name = update["message"]["from"]["last_name"]
            except:
                last_name = ''
            try:
                username = update["message"]["from"]["username"]
            except:
                username = ''

            message_id = update["message"]["message_id"]
            if message_text == '/gete':
                user_id = user_id
                pi = get_point(user_id)
                send_message('' + str(pi), chat_id, message_id)
            elif message_text.startswith('/add-') and update["message"]['reply_to_message'] and str(user_id) in list:
                repy_id = update["message"]['reply_to_message']['from']['id']
                string = str(message_text)
                pattern = '\d+'
                result = re.findall(pattern, string)
                print(result)
                add = str(result[0])
                asd = add_point(repy_id, add)
                send_message('\n https://t.me/eng_hasan97 \n\nThe number of your chances : ' + str(asd), chat_id,
                             message_id)
            elif message_text == "/zero" and update["message"]['reply_to_message'] and str(user_id) in list:
                repy_id = update["message"]['reply_to_message']['from']['id']
                zz = zro(repy_id)
                print(str(zz))
                send_message("Total points have been deleted : \n\n https://t.me/eng_hasan97", chat_id, message_id)
            elif message_text == "/infoe" and str(user_id) in list:
                send_message('The number of database  :' + str(mycol.count()), chat_id, message_id)
            elif message_text == "/ide":
                send_message("id :" + str(user_id) + "\n" + str(chat_id), chat_id, message_id)
            elif message_text.startswith('/alle-') and str(user_id) in list:
                string = str(message_text)
                pattern = '\d+'
                result = re.findall(pattern, string)
                print(result)
                add = str(result[0])
                all4add(add)
                send_message('Chances are increased for everyone: ' + str(add), chat_id, message_id)
            elif message_text == "/allzeroe":
                add = "0"
                all4sub(add)
                send_message("Total points have been deleted \n\n https://t.me/eng_hasan97", chat_id, message_id)
            elif message_text.startswith('/sub-alle-') and str(user_id) in list:
                string = str(message_text)
                pattern = '\d+'
                result = re.findall(pattern, string)
                print(result)
                add = str(result[0])
                all4subb(add)
                send_message('Chances are sub for everyone: ' + str(add), chat_id, message_id)




            elif 'text' in update['message'].keys():
                if message_text == '/start':
                    send_message('Bot is working successfully ☺\n ', chat_id)
                    return True

                if 'entities' in update['message'].keys():
                    qu_url = ''
                    for entiti in update['message']['entities']:
                        if (entiti['type'] == 'url' or entiti['type'] == 'text_link'):
                            offset = entiti['offset']
                            length = entiti['length']
                            qu_url = message_text[offset: offset + length]

                    if qu_url:
                        print("Question : ", qu_url)
                        if str(chat_type) == 'supergroup' or str(chat_type) == 'group':
                            if qu_url.startswith(
                                    "https://www.bartleby.com/questions-and-answers/") or qu_url.startswith(
                                    "https://www.bartleby.com/solution-answer/chapter"):
                                print("url bartleby")
                                r = requests.get(str(qu_url), headers=headers, data=payload)
                                soup = s(r.content, 'html.parser')
                                print(r)
                                print(soup.text)
                                
                                if "This question hasn’t" in str(soup.text):
                                    send_message(
                                        '⚠️لم يتم حل السؤال ...تحقق من الرابط\n Your question has not been solved yet ..... ⚠️',chat_id, message_id)
                                elif "Don't worry! We won't leave you hanging. Plus, we're giving you back one question for the inconvenience." in str(
                                        soup.text):
                                    send_message('تم حذف سوالك من قبل الموقع ...Your question has been deleted',
                                                 chat_id, message_id)
                                else:
                                    print("now l can get your answers")
                                    pi = get_point(user_id)
                                    print(pi)
                                    ress = int(pi)
                                    if ress == 0 or ress < 0:
                                        send_message('You do not have points', chat_id, message_id)
                                    else:
                                        if 'https://www.bartleby.com/questions-and-answers' in qu_url:
                                            images4 = soup.find_all("script")
                                            # print(images4)

                                            text = str(images4)
                                            start = text.find('''questionId''') + 13
                                            end = text.find('''","createdDate''')
                                            cut_text2 = text[start:end].strip()
                                            print(cut_text2)
                                            #############
                                            text2 = str(images4)
                                            start = text2.find('''accessToken''') + 14
                                            end = text2.find('''","refreshToken''')
                                            cut_text3 = text2[start:end].strip()
                                            print(cut_text3)

                                            ################
                                            url = "https://nk6xemh85d.execute-api.us-east-1.amazonaws.com/prod/qna/answer/" + str(
                                                cut_text2)
                                            ####################
                                            headers8 = {
                                                'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0',
                                                'Accept': '*/*',
                                                'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
                                                'Referer': 'https://www.bartleby.com/',
                                                'authorization': 'Bearer ' + str(cut_text3),
                                                'Origin': 'https://www.bartleby.com',
                                                'Connection': 'keep-alive',
                                                'Sec-GPC': '1',
                                                'TE': 'Trailers'
                                            }

                                            response = requests.request("GET", url, headers=headers8, data=payload)
                                            print(response.text)
                                            # response.json()['data']['answer']['steps'][2]['text']
                                            xx = response.json()['data']['answer']['numberOfAnswerSteps']
                                            xx2 = response.json()['data']['question']['text']
                                            # print(response.json()['data']['question']['images'][0]['imageUrl'])

                                            for i in range(xx):
                                                # ff
                                                f = open('DDbb.html', 'a')
                                                f.write("""<H3> <p style="color:RED;">""" + "Step " + str(
                                                    i + 1) + " of " + str(xx) + ":) </H3> </p>" + "\n" + str(
                                                    response.json()['data']['answer']['steps'][i]['text']))
                                                f.close()

                                            #############
                                            if "images': []" not in str(
                                                    response.json()['data']['question']) and """'text': None""" in str(
                                                    response.json()['data']['question']):
                                                print("is img")
                                                f2 = open('DDbb.html', 'r')
                                                f = open('Answer.html', 'w')
                                                f.write(
                                                    """
                    <html><head>
                 <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
                                           <meta charset="UTF-8"><html><head><link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css"><link rel="preconnect" href="https://fonts.gstatic.com"><link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet"><link rel = "stylesheet" type = "text/css" href = "https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.9.0/katex.min.css" /><link href="https://fonts.googleapis.com/css2?family=Baloo+Bhaina+2:wght@600&display=swap" rel="stylesheet"></head><body><style>.x {background-color: white;border:solid red 5px; }.y {background-color: white;border:solid green 5px;}.x img{max-width: 100%;max-height: 100%;margin: auto;display: block;}.y img{ max-width: 100%; max-height: 100%; margin: auto; display: block; }  .highlighted-text {background-image: url('data:');  </style> <link rel="preconnect" href="https://fonts.gstatic.com"> <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet"> <link rel = "stylesheet" type = "text/css" href = "https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.9.0/katex.min.css" /> <link href="https://fonts.googleapis.com/css2?family=Baloo+Bhaina+2:wght@600&display=swap" rel="stylesheet"> <h1> <div class="tele"> <div class="center"> <center><strong><div><p>Solution obtained by STUDENT SERVICES</p> </div> <div class="center" ><center><strong> <img src="https://blogger.googleusercontent.com/img/a/AVvXsEg9LnL_z1-JsSaZPeLeHPnLY8P4XSAHt7vaSOuGsuFpFJOVznOr4cj-0zi5hc5yqUPiGH2CuBsgTd2GKjRNS2GssNy6Mkk_sdkrbpzS8YW0HcY3YACznWdzG47me34UNhfcUDeU0iMmDGPY9d1EYu4JHiDrDUxndUchHDqdae9F3e5OBwiNKKtJFo6RuQ=s228"> 
<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">×</span></button>
                                            <center><strong> <p><a href="https://t.me/eng_hasan97"> Answers bartleby by HASSAN NAZZAL : @lq_bc</a></p></strong>
                                            </div> <span class="group_title"></span> <div class="tgme_page_extra"></div><p><span class="highlighted-text"></span> </p></div> <center><strong> <p><a href="https://t.me/eng_hasan97"> All Answers by hassannazzal : dev </a></p></strong>
                                            </div> <div> </div> </div> </h1> <h1> <p> <div class="center">            
                                                </div>
                                            </div>
                                            </h1>
                                              <h1>
                                                <p>
                                                    <div class="nn"
                                                     align="center">Your Question
                                                    </div>
                                                </p>
                                            </h1>
                                        <div class="x" align="center"> """ + str(
                                                        "") + ":) </H1> </p>" + "\n" + str(
                                                        "<img src=" + response.json()['data']['question']['images'][0][
                                                            'imageUrl'] + """>""") + "\n\n" + """</div>
                                            </div>
                                              <h1>
                                                <p>
                                                    <div class="a"
                                                     align="center">Your Answer
                                                    </div>
                                                </p>
                                            </h1>
                                            <div class="y">
                                        </div>""" + "\n\n" + f2.read() + str(
                                                        hh2))
                                                f.close()

                                            elif "images': []" in str(response.json()['data'][
                                                                          'question']) and """'text': None""" not in str(
                                                    response.json()['data']['question']):
                                                print("is text")
                                                f2 = open('DDbb.html', 'r')
                                                f = open('Answer.html', 'w')
                                                f.write(
                                                    """
                    <html><head>
                 <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
                                           <meta charset="UTF-8"><html><head><link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css"><link rel="preconnect" href="https://fonts.gstatic.com"><link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet"><link rel = "stylesheet" type = "text/css" href = "https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.9.0/katex.min.css" /><link href="https://fonts.googleapis.com/css2?family=Baloo+Bhaina+2:wght@600&display=swap" rel="stylesheet"></head><body><style>.x {background-color: white;border:solid red 5px; }.y {background-color: white;border:solid green 5px;}.x img{max-width: 100%;max-height: 100%;margin: auto;display: block;}.y img{ max-width: 100%; max-height: 100%; margin: auto; display: block; }  .highlighted-text {background-image: url('data:');  </style> <link rel="preconnect" href="https://fonts.gstatic.com"> <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet"> <link rel = "stylesheet" type = "text/css" href = "https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.9.0/katex.min.css" /> <link href="https://fonts.googleapis.com/css2?family=Baloo+Bhaina+2:wght@600&display=swap" rel="stylesheet"> <h1> <div class="tele"> <div class="center"> <center><strong><div><p>Solution obtained by STUDENT SERVICES</p> </div> <div class="center" ><center><strong> <img src="https://blogger.googleusercontent.com/img/a/AVvXsEg9LnL_z1-JsSaZPeLeHPnLY8P4XSAHt7vaSOuGsuFpFJOVznOr4cj-0zi5hc5yqUPiGH2CuBsgTd2GKjRNS2GssNy6Mkk_sdkrbpzS8YW0HcY3YACznWdzG47me34UNhfcUDeU0iMmDGPY9d1EYu4JHiDrDUxndUchHDqdae9F3e5OBwiNKKtJFo6RuQ=s228"> 
<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">×</span></button>
                                            <center><strong> <p><a href="https://t.me/eng_hasan97">For All Answers bartleby by HASSAN NAZZAL : @lq_bc</a></p></strong>
                                            </div> <span class="group_title"></span> <div class="tgme_page_extra"></div><p><span class="highlighted-text"></span> </p></div> <center><strong> <p><a href="https://t.me/eng_hasan97">For All Answers chegg Join group : chegg_So</a></p></strong>
                                            </div> <div> </div> </div> </h1> <h1> <p> <div class="center">            
                                                </div>
                                            </div>
                                            </h1>
                                              <h1>
                                                <p>
                                                    <div class="nn"
                                                     align="center">Your Question
                                                    </div>
                                                </p>
                                            </h1>
                                        <div class="x" align="center"> """ + str(
                                                        "") + ":) </H1> </p>" + "\n\n" + str(
                                                        xx2) + "\n" + """</div>
                                            </div>
                                              <h1>
                                                <p>
                                                    <div class="a"
                                                     align="center">Your Answer
                                                    </div>
                                                </p>
                                            </h1>
                                            <div class="y">
                                        </div>""" + "\n\n" + str(
                                                        "") + "\n" + f2.read() + str(hh2))
                                                f.close()
                                            else:
                                                print(" img and text")
                                                f2 = open('DDbb.html', 'r')
                                                f = open('Answer.html', 'w')
                                                f.write(
                                                    """
                    <html><head>
                 <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
                                           <meta charset="UTF-8"><html><head><link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css"><link rel="preconnect" href="https://fonts.gstatic.com"><link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet"><link rel = "stylesheet" type = "text/css" href = "https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.9.0/katex.min.css" /><link href="https://fonts.googleapis.com/css2?family=Baloo+Bhaina+2:wght@600&display=swap" rel="stylesheet"></head><body><style>.x {background-color: white;border:solid red 5px; }.y {background-color: white;border:solid green 5px;}.x img{max-width: 100%;max-height: 100%;margin: auto;display: block;}.y img{ max-width: 100%; max-height: 100%; margin: auto; display: block; }  .highlighted-text {background-image: url('data:');  </style> <link rel="preconnect" href="https://fonts.gstatic.com"> <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet"> <link rel = "stylesheet" type = "text/css" href = "https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.9.0/katex.min.css" /> <link href="https://fonts.googleapis.com/css2?family=Baloo+Bhaina+2:wght@600&display=swap" rel="stylesheet"> <h1> <div class="tele"> <div class="center"> <center><strong><div><p>Solution obtained by STUDENT SERVICES</p> </div> <div class="center" ><center><strong> <img src="https://blogger.googleusercontent.com/img/a/AVvXsEg9LnL_z1-JsSaZPeLeHPnLY8P4XSAHt7vaSOuGsuFpFJOVznOr4cj-0zi5hc5yqUPiGH2CuBsgTd2GKjRNS2GssNy6Mkk_sdkrbpzS8YW0HcY3YACznWdzG47me34UNhfcUDeU0iMmDGPY9d1EYu4JHiDrDUxndUchHDqdae9F3e5OBwiNKKtJFo6RuQ=s228"> 
<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">×</span></button>
                                            <center><strong> <p><a href="https://t.me/eng_hasan97">For All Answers bartleby Join group : @https://t.me/eng_hasan97 @lq_bc</a></p></strong>
                                            </div> <span class="group_title"></span> <div class="tgme_page_extra"></div><p><span class="highlighted-text"></span> </p></div> <center><strong> <p><a href="https://t.me/eng_hasan97">For All Answers chegg Join group : chegg_So</a></p></strong>
                                            </div> <div> </div> </div> </h1> <h1> <p> <div class="center">            
                                                </div>
                                            </div>
                                            </h1>
                                              <h1>
                                                <p>
                                                    <div class="nn"
                                                     align="center">Your Question
                                                    </div>
                                                </p>
                                            </h1>
                                        <div class="x" align="center"> """ + str(
                                                        "") + ":) </H1> </p>" + "\n\n" + str(xx2) + "\n" + str(
                                                        "<img src=" + response.json()['data']['question']['images'][0][
                                                            'imageUrl'] + """>""") + "\n\n" + """</div>
                                            </div>
                                              <h1>
                                                <p>
                                                    <div class="a"
                                                     align="center">Your Answer
                                                    </div>
                                                </p>
                                            </h1>
                                            <div class="y">
                                        </div>""" + "\n\n" + f2.read() + str(
                                                        hh2))
                                                f.close()
                                            os.remove("DDbb.html")
                                            su = sub_point(user_id)
                                            pi = get_point(user_id)
                                            i = open('./Answer.html', 'rb')

                                            url876 = (
                                                        "https://api.telegram.org/bot" + TOKEN + "/sendDocument?chat_id=" + str(
                                                    chat_id) + '&caption=' + str(
                                                    "🌚 هذا الحل @lq_bc") + '&reply_to_message_id=' + str(
                                                    message_id) + '&parse_mode=Markdown')
                                            url_txt = requests.post(url876, files={'document': i})

                                        # print(response.json()['data']['question'])

                                        else: 
                                            f = open("Answer.html", "w")
                                            f.write(str(soup))
                                            f.close()
                                            su = sub_point(user_id)
                                            pi = get_point(user_id)
                                            i = open('./Answer.html', 'rb')

                                            url876 = (
                                                        "https://api.telegram.org/bot" + TOKEN + "/sendDocument?chat_id=" + str(
                                                    chat_id) + '&caption=' + str(
                                                    "🌚 هذا الحل @lq_bc") + '&reply_to_message_id=' + str(
                                                    message_id) + '&parse_mode=Markdown')
                                            url_txt = requests.post(url876, files={'document': i})

                        else:
                            send_message("Bot only works in groups", chat_id, message_id)




    except:
        exc_type, exc_obj, tb = sys.exc_info()
        f = tb.tb_frame
        lineno = tb.tb_lineno
        filename = f.f_code.co_filename
        linecache.checkcache(filename)
        line = linecache.getline(filename, lineno, f.f_globals)
        print('Error EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj))
    return True



def send_req(qurl, email):
    try:
        print("p")
    except:
        pass


def editMessage(text, chat_id, text_id, inline_keyboard):
    try:
        url = URL + "editMessageText?chat_id={}&message_id={}&parse_mode=&text={} &reply_markup=".format(chat_id,
                                                                                                         text_id,
                                                                                                         text) + inline_keyboard
        r = get_url(url)
        return r
    except:
        pass


def deleteMessage(chat_id, message_id):
    try:
        url = URL + "deleteMessage?chat_id={}&message_id={}".format(chat_id, message_id)
        get_url(url)
    except:
        pass


def send_message(text, chat_id, text_id=None, inline_keyboard=None, parse_mode=None):
    try:
        data = {
            'text': text,
            'chat_id': chat_id,
            'reply_to_message_id': text_id,
            'reply_markup': inline_keyboard,
            'disable_web_page_preview': True,
            'parse_mode': parse_mode
        }
        r = post_url(URL + "sendMessage", data)
        return r
    except Exception as e:
        print(e)


def main():
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        # print(updates)
        try:
            if len(updates["result"]) > 0:
                last_update_id = get_last_update_id(updates) + 1
                for i in updates['result']:
                    Check(i)
        except:
            try:
                print(updates['description'])
            except:
                pass


if __name__ == '__main__':
    main()