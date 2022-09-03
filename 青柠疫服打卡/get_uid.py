import requests
from hashlib import md5

xuehao = "" #学号
xingming = "" #姓名
mima = "" #密码

mimamd5 = md5(mima.encode('utf8')).hexdigest()
formdata = {
    "YXDM":"10623",
    "UserType":"1",
    "XGH":xuehao,
    "Name":xingming,
    "PassWord":mimamd5
    }
url = "https://yqfkapi.zhxy.net/api/User/CheckUser"
headers={ "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
session = requests.session()
response = session.post(url, data = formdata, headers = headers)
print(response.text)
json_response = response.json()
try:
 UID = json_response['data']['ID']
 print("账号密码验证成功，获取到UID="+str(UID))
except:
 error = json_response['info']
 print(xuehao+"登录失败："+error)
