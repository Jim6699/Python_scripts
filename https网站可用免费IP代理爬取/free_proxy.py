import requests
from sqlalchemy import all_
from fake_useragent import UserAgent
 
def get_proxy():
    return requests.get("http://demo.spiderpy.cn/get/").json()
def confirm_proxy():
    ip = requests.get('http://httpbin.org/ip')
    my_ip = (ip.json())["origin"]
    print("本地IP：{}".format(my_ip))
    retry_count = 100
    proxies_list = []
    false_list = []
    while retry_count > 0:
        retry_count -= 1
        proxy = get_proxy().get("proxy")
        #print(proxy)
        if proxy in proxies_list or proxy in false_list:
            #print("该代理 {} 已经在列表中，跳过!".format(proxy))
            continue
        try:
            headers= {'User-Agent':str(UserAgent(verify_ssl=False).random)}
            html = requests.get('https://www.taobao.com/help/getip.php', proxies={"https": "https://{}".format(proxy)}, headers=headers, timeout=30)
            print(html.text)
            if html.status_code == 200:
                if (proxy.split(":")[0] in html.text) != my_ip:
                    print("代理 {} 请求成功".format(proxy))
                    proxies_list.append(proxy)
        except Exception:
            false_list.append(proxy)
            #print("代理 {} 请求失败".format(proxy))
    return proxies_list
 
sumlist = confirm_proxy()
print("="*20)
print("全部检索完毕！\n可用IP代理如下：")
print(sumlist)
print("="*20)
