import requests
import random
import time
import json
from urllib import parse
user_agent_list = ["Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/61.0",
                    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
                    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
                    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
                    "Mozilla/5.0 (Macintosh; U; PPC Masc OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
                    ]
def add(ua,time_string):
    URL = "http://xreport.uwewe.cn/click/add"
    headers = {
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'User-Agent': ua,
        'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
        'Content-Length': '126',
        'Host': 'xreport.uwewe.cn',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip'
        }
    print(headers)
    FormData = {"event":"signin","place":"WebActivity","time":time_string,"type":"签到","typeEN":"signin","plat":"android","version":"10011"}
    data = parse.urlencode(FormData)
    print(data)
    html = requests.post(url=URL, data=data, headers=headers)
    print(html.text)
    return html.text

def sign(ua,userId):
    URL = "http://xconfig.uwewe.cn/sign/signvideoClient"
    headers = {
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'User-Agent': ua,
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '39',
        'Host': 'xconfig.uwewe.cn',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip'
        }
    print(headers)
    FormData = {"userId":userId,"extra":"android-10011-102"}
    data = parse.urlencode(FormData)
    print(data)
    html = requests.post(url=URL, data=data, headers=headers)
    print(html.text)
    return html.text

def pushplus_sms(token,userId,alltxt):
    headers={
        "User-Agent":"Mozilla/5.0 (Linux; Android 9; SM-A102U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.93 Mobile Safari/537.36",
        "Content-Type": "application/json"
        }
    url="http://www.pushplus.plus/send"
    data={
        "token":token,
        "title":f"{userId}微微电话签到",
        "content":str(alltxt),
        "template":"txt"
        }
    res = requests.post(url=url,params=data,headers=headers)
    print(res.text)
    
    
def main():
    
    token = "" #请输入pushplus给你的Token，用于接受程序签到通知
    userId_list = ["",] #账号信息，自行抓取|可多账号，也可单一账号，自行修改
    
    for userId in userId_list:
        print("="*20)
        print(f"准备签到：{userId}")
        time_string = time.strftime("%Y-%m-%d %X", time.localtime()).replace(" ","")
        print(time_string)
        ua = random.choice(user_agent_list)
        print(ua)
        a = add(ua,time_string)
        b = sign(ua,userId)
        alltxt = str(a)+"+"+str(b)
        print(alltxt)
        pushplus_sms(token,alltxt)

def main_handler(event, context):
    return main()
if __name__ == '__main__':
    main()
