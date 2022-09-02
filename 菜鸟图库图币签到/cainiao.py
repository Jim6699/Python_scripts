import requests
import json

def gostart():
    def qiandao():
        headers ={
            "cookie": ck,
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
            }
        qiandao = requests.get(url="https://www.sucai999.com/default/qiandao/qd",headers=headers)
        ret = qiandao.text.encode('ascii').decode('unicode_escape')
        print(ret)
        return ret
    '''
    请填写以下信息
    '''
    name = "" #方便你识别的标记
    token = "" #pushplus公众号给你的token
    ck = "" #菜鸟图库登录后浏览器缓存的cookie，随便一个url请求标头都有，基本取一次永久使用
    
    print("------签到系统------")
    try:
        news1 = qiandao()
    except:
        news1 = "error"

    print("------------------------")
    txt = "<h18>账号：{}</h18><br><h18>签到结果：{}</h18><br><h18>-------</h18><br>".format(name,news1)

    try:
        headers={
            "User-Agent":"Mozilla/5.0 (Linux; Android 9; SM-A102U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.93 Mobile Safari/537.36",
            "Content-Type": "application/json"
            }
        url="http://www.pushplus.plus/send"
        data={
            "token":token,
            "title":"@菜鸟图库签到",
            "content":str(txt),
            "template":"html"
            }
        res = requests.post(url=url, json=data, headers=headers)
        print(res.status_code)
        out = "发送通知成功"
        #print(out)
    except:
        out = "发送通知失败"
    return out

def main():
    gostart()
def main_handler(event, context):
    return main()
if __name__ == '__main__':
    main()

