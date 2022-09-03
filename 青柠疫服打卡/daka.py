import pandas as pd
import time
import json
import requests
import base64
from hashlib import md5
import random
import ddddocr

def jiancha(stu_uid,YXDM):
    daka_url = 'https://yqfkapi.zhxy.net/api/ClockIn/IsClockIn?uid={}&usertype=1&yxdm={}'.format(stu_uid,YXDM)
    print("专属检查链接为："+str(daka_url))
    daka = s.get(daka_url)
    print(daka.text)
    json_response = daka.json()
    try:
        a = json_response["data"]["msg"]
        print("打卡信息检查："+a)
    except:
        a = "打卡信息检查：大概率访问频繁"
        print(a)
    return a

def dddocr():
    pic1 = s.get('https://yqfkapi.zhxy.net/api/common/getverifycode')
    tex1 = pic1.content
    tex2 = bytes.decode(tex1)
    if json.loads(tex2)['info'] == '非法访问！':
        print(tex2)
        sys.exit(1)
    tex3 = json.loads(tex2)['data']['img']
    key = json.loads(tex2)['data']['key']
    print("获取到验证码img:"+tex3)
    print("获取到验证码key:"+key)
    imgData = base64.b64decode(tex3)
    print("验证码base64编码："+str(imgData))
    print("准备启动ddddocr")
    ocr = ddddocr.DdddOcr()
    print("准备识别验证码")
    code = str(ocr.classification(imgData))
    print("识别到验证码code："+code)
    return key,code

def qiandao(stu_uid,JWD,key,code,position,YXDM):
    data_health = {
        "UID": stu_uid,
        "UserType": "1",
        "JWD": JWD,
        "key": key,
        "code": code,
        "ZZDKID": "37",
        "A1": "正常",
        "A4": "无",
        "A2": "全部正常",
        "A3": position,
        "A11": "在校",
        "A12": "未实习",
        "A13": "低风险区",
        "YXDM": YXDM,
        "version": "v1.3.2"
        }
    print(data_health)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
    health_result = s.post('https://yqfkapi.zhxy.net/api/ClockIn/Save', json=data_health, headers=headers)
    json_response = health_result.json()
    print(json_response)
    b = json_response["info"]
    return str(b)

def pushdeer(push_key,sendnews):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36'}
    urltxt = "https://api2.pushdeer.com/message/push?pushkey={}&text={}".format(push_key,sendnews)
    page = requests.get(url=urltxt, headers=headers)
    print("已经打卡情况进行pushdeer推送！")

def send_pusher(root_push_key,times):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36'}
    urltxt = "https://api2.pushdeer.com/message/push?pushkey={}&text={}".format(root_push_key,times)
    page = requests.get(url=urltxt, headers=headers)
    return "管理员send_pusher操作结束"
        
def main_handler():
    global s
    s = requests.Session()
    print("-------------执行打卡程序中-------------")
    '''
    下面3个参数需要手动填写
    '''
    YXDM = "" #学校代码
    JWD = "" #学校经纬度位置，打开https://jim6699.github.io/some_useful/qingningyifu_get_position.html定位均可
    root_push_key = "" #管理员的Pushdeer密钥
    
    chenggongtimes = 0
    shibaitimes = 0
    data = pd.read_csv("青柠打卡账号.csv", encoding = 'utf-8')
    lis = []
    for i in range(data.shape[0]):
        line = data.loc[i]
        lis.append(dict(line))

    for i in lis:
        stu_name = str(i["stu_name"])
        print(stu_name)
        stu_uid = str(i["stu_uid"])
        print(stu_uid)
        push_key = str(i["push_key"])
        print(push_key)
        position = str(i["position"])
        print(position)

        jiancha(stu_uid,YXDM)
        try:
            print("-------------执行打卡程序中-------------")
            key,code = dddocr()
            time.sleep(5)
            qian = qiandao(stu_uid,JWD,key,code,position,YXDM)
            print(str(qian))
            if qian == "响应成功" or qian == "今天你已经自诊打过卡了！":
                chenggongtimes += 1  
            else:
                m = 0
                while qian in  "操作失败，验证码错误":
                    m += 1
                    print(stu_name+"|打卡出现问题："+qian+"|重试识别验证码第"+str(m)+"次")
                    if m <= 4:
                        jiancha(stu_uid,YXDM)
                        key,code = dddocr()
                        time.sleep(5)
                        qian = qiandao(stu_uid,JWD,key,code,position,YXDM)
                    else:
                        shibaitimes += 1
                        qian = "注意！请自己手动去打卡吧|https://wxyqfk.zhxy.net/?yxdm=10623&from=singlemessage#/clockIn"
                        break
                    
            sendnews = f"青柠打卡反馈：{position} |"+stu_name+"："+qian
            print(sendnews)
            pushdeer(push_key,sendnews)
        except:
            print("@ 遇见问题")

        randomInt = random.randint(10,15) 
        print("将等待：" + str(randomInt) + " 秒")
        time.sleep(randomInt)
            
        
    times = "管理员：在校打卡系统|成功打卡{}人，失败打卡{}人".format(chenggongtimes,shibaitimes)
    print(times)
    pusher_onwer = send_pusher(root_push_key,times)
    print(pusher_onwer)
    print("-------------结束-------------")
    return "全部结束"

if __name__ == "__main__":
    start = main_handler()
    print(start)

