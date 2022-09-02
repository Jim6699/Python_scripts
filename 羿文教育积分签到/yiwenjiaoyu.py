import requests
import hashlib
import json
import time
def gostart():
    def key(password):
        hl = hashlib.md5()
        hl.update(password.encode(encoding="utf-8"))
        password = hl.hexdigest()
        return password
    def qiandao(CK):
        #签到API
        URL = "https://proxyweb.yiwenjy.com/yiwen_pc/add_userSign"
        headers ={
            'Accept': 'application/json',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Authorization': CK,
            'Connection': 'keep-alive',
            'Content-Length': '0',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'proxyweb.yiwenjy.com',
            'Origin': 'https',
            'Referer': 'https',
            'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44'
            }
        qiandao = requests.post(url=URL, json=None, headers=headers)
        a = qiandao.text
        print(a)
        return a
    def chaxun(CK):
        #查询API
        URL = "https://proxyweb.yiwenjy.com/yiwen_pc/query_sumPoint"
        headers ={
            'Accept': 'application/json',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Authorization': CK,
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'proxyweb.yiwenjy.com',
            'Origin': 'https',
            'Referer': 'https',
            'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44'
            }
        points = requests.get(url=URL, headers=headers)
        b = points.text
        print(b)
        return b
    def denglu(userPhone,md5_password):
        #登录API
        URL = "https://proxyweb.yiwenjy.com/yiwen_pc/login_by_pwd"
        headers ={
            'Accept': 'application/json',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Connection': 'keep-alive',
            'Content-Length': '63',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'proxyweb.yiwenjy.com',
            'Origin': 'https',
            'Referer': 'https',
            'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44'
            }
        da = {
            "userPhone": userPhone,
            "password": md5_password
            }
        login = requests.post(url=URL,data=da,headers=headers)
        print(login.text)
        json_response = login.json()
        try:
            result = json_response["data"]["token"]
            CK = str(result)
            print(CK)
        except:
            CK = json_response
        print(CK)
        return CK
    def pushdeer(pushdeer_key,sendnews):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36'}
        urltxt = "https://api2.pushdeer.com/message/push?pushkey={}&text={}".format(pushdeer_key,sendnews)
        page = requests.get(url=urltxt, headers=headers)
        print("已经打卡情况进行pushdeer推送！")
 
    #请手动填写以下三行信息
    userPhone = "" #手机号
    password = "" #明文密码
    pushdeer_key = "" #pushdeer的key
 
    
    md5_password = key(password)
    print("="*30)
    print("手机号码：" + userPhone)
    print("加密密码：" + md5_password)
    print("="*30)
    print("打卡运行中...")
    CK1 = denglu(userPhone,md5_password)
    alltxt_1 = qiandao(CK1)
    alltxt_2 = chaxun(CK1)
    alltxt = str(alltxt_1) + str(alltxt_2)
    pushdeer(pushdeer_key,alltxt)
    print("运行结束")
 
def main():
    gostart()
def main_handler(event, context):
    return main()
if __name__ == '__main__':
    main()
