import requests
import time

def login(phone,password):
    login_url = "https://dcxy-customer-app.dcrym.com/app/customer/login"
    headers = {
        'Host': 'dcxy-customer-app.dcrym.com',
        'accept-language': 'zh-CN,zh;q=0.8',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; PCT-AL10 Build/HUAWEIPCT-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045409 Mobile Safari/537.36 MMWEBID/5981 MicroMessenger/7.0.20.1781(0x2700143D) Process/tools WeChat/arm64 NetType/4G Language/zh_CN ABI/arm64',
        'token': '',
        'key': 'test',
        'reqsource': 'app',
        'clientsource': '{"areaId"',
        'content-type': 'application/json',
        'content-length': '54',
        'accept-encoding': 'gzip',
        'clientsource':'{"areaId": "","customerId": "","uuid": "358692865688245","sourceType": "Android","appVersion": "4.3.91","platformCode": "00001","systemVersion": "28","deviceInfo": "HUAWEI VOG-AL00","networkInfo": " WIFI"}'
        }
    login_data ={
        "loginAccount": phone,
        "password": password
        }
    html = requests.post(url=login_url,json=login_data, headers=headers)
    #print(html.text)
    json_response = html.json()
    ck = json_response["data"]["token"]
    customerId = json_response["data"]["customerId"]
    customerName = json_response["data"]["customerName"]
    campusId = json_response["data"]["areaId"]
    return ck,customerId,customerName,campusId

def get_devices(clientsource,customerId,ck,campusId):
    url = "https://gx-app-server.dcrym.com/dcxy/api/gx/devices/lastUsedByCurrentUser?customerId={}&campusId={}".format(customerId,campusId)
    #print(url)
    headers = {
        'Host': 'gx-app-server.dcrym.com',
        'accept-language': 'zh-CN,zh;q=0.8',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; PCT-AL10 Build/HUAWEIPCT-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045409 Mobile Safari/537.36 MMWEBID/5981 MicroMessenger/7.0.20.1781(0x2700143D) Process/tools WeChat/arm64 NetType/4G Language/zh_CN ABI/arm64',
        'token': ck,
        'key': 'test',
        'reqsource': 'app',
        'clientsource': str(clientsource),
        'content-type': 'application/json',
        'accept-encoding': 'gzip'
        }
    #print(headers)
    html = requests.get(url=url,headers=headers)
    #print(html.text)
    json_response = html.json()
    devices_list = json_response["data"]
    #print(devices_list)
    devices_dict = {}
    for i in devices_list:
        position = i["position"]
        code = i["code"]
        devices_dict[position] = code
    print("该账号曾用饮水机：")
    print(devices_dict)
    try:
        shibai = 0
        for m in devices_dict:
            #print(m)
            if where in m:
                print("模糊匹配成功！")
                print("标准定位：" + m)
                print("设备号：" + devices_dict[m])
                return devices_dict[m]
            else:
                shibai += 1
        if shibai == len(devices_dict):
            print("模糊匹配失败！将手动确认，请根据标准定位选择对应设备号！")
            for m in devices_dict:
                print("*"*20)
                print("标准定位：" + m) 
                print("设备号：" + devices_dict[m])
            choice = input("请手动输入对应的设备号：")
            return choice            
    except Exception as e:
        print(e)
        print("遇见问题！将手动确认，请根据标准定位选择对应设备号！")
        for m in devices_dict:
            print("*"*20)
            print("标准定位：" + m) 
            print("设备号：" + devices_dict[m])
        choice = input("请手动输入对应的设备号：")
        return choice
                
def kaiqi(clientsource,devices,customerId,customerName,phone,ck,campusId):
    url = "https://gx-app-server.dcrym.com/dcxy/api/gx/devices/{}/beginning".format(devices)
    data ={
      "customerId": customerId,
      "customerName": customerName,
      "customerPhone": phone,
      "campusId": campusId
      }
    #print(data)
    headers = {
        'Host': 'gx-app-server.dcrym.com',
        'accept-language': 'zh-CN,zh;q=0.8',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; PCT-AL10 Build/HUAWEIPCT-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045409 Mobile Safari/537.36 MMWEBID/5981 MicroMessenger/7.0.20.1781(0x2700143D) Process/tools WeChat/arm64 NetType/4G Language/zh_CN ABI/arm64',
        'token': ck,
        'key': 'test',
        'reqsource': 'app',
        'clientsource': str(clientsource),
        'content-type': 'application/json',
        'content-length': '98',
        'accept-encoding': 'gzip'
        }

    html = requests.post(url=url,json=data,headers=headers)
    print(html.text)
    return "开启！"
def main():
    #手机号
    phone = ""
    #密码
    password = ""
    #机器位置(知道的话就写，不知道的话运行一遍你就知道标准位置，再替换|扫码饮水里面可以看见最近使用机器位置和编号）
    where = ""


    print("="*20)
    print("多彩校园-快捷开水系统 启动...")
    print("账号：" + phone)
    print("密码：" + password)
    print("饮水机所在位置（粗匹配）：" + where)
    print("="*20)
    print("准备登录")
    ck,customerId,customerName,campusId = login(phone,password)
    print("登录结束")
    print("="*20)
    time.sleep(0.5)
    clientsource = {
        "areaId": "{}".format(campusId),
        "customerId": "{}".format(customerId),
        "uuid": "358692865688245",
        "sourceType": "Android",
        "appVersion": "4.3.91",
        "platformCode": "00001",
        "systemVersion": "28",
        "deviceInfo": "HUAWEI VOG-AL00",
        "networkInfo": " WIFI"
        }
    print("准备获取饮水机设备号")
    devices = get_devices(clientsource,customerId,ck,campusId)
    print(f"将启动饮水机：{devices}")
    print("获取饮水机设备号结束")
    print("="*20)
    print("准备启动饮水机")
    b = kaiqi(clientsource,devices,customerId,customerName,phone,ck,campusId)
    print("启动饮水机结束")
    print("="*20)
    
if __name__ == "__main__":
    main()
