import requests
from urllib import parse

def call(userId,phone,called,pwd,validate):
    URL = "http://xcallback.uwewe.cn/callback.aspx"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '151',
        'Host': 'xcallback.uwewe.cn',
        'Connection': 'Keep-Alive'
        }
    FormData = {"weweid":userId,"caller":phone,"called":called,"pwd":pwd,"validate":validate,"plat":"android","lau":"1"}
    data = parse.urlencode(FormData)
    print(data)
    html = requests.post(url=URL, data=data, headers=headers)
    print(html.text)
    return html.text

    
    
def main():
    '''
    APP发起通话时候，选择"专线电话拨打"，抓包能全部抓到以下信息，貌似pwd和validate可永久使用，即是重新登陆了旧的这些信息还是有用，待测！
    '''
    userId = "" #账号信息，自行抓取
    phone = "" #你的手机号码，phone要对应userId
    called = "" #必填|仅做电话提醒可输自己另外手机号|做免费电话请输入朋友号码
    pwd = "" #pwd密码信息，自行抓取
    validate = "" #validate信息，自行抓取

    tixing = call(userId,phone,called,pwd,validate)
    print("="*30)
    if "msg" in tixing:
        print("呼叫成功")
    elif "余额不足" in tixing:
        print("呼叫失败|余额不足，多签到几天吧！")
    elif "<error>验证失败</error>" in tixing:
        print("呼叫失败|pwd or validate 不正确！")
    else:
        print("呼叫失败|其他原因")

def main_handler(event, context):
    return main()
if __name__ == '__main__':
    main()
