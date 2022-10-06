## python批量查看/下载牛客网在线测评答案
##### 1.该软件仅供技术交流使用，禁止用于任何违法违规行为，否则后果自负，请遵纪守法!
##### 2.该软件不会重复提交请求，不会增加牛客网服务器压力，不会影响牛客网服务器正常运行。
###### 基本我把行测的题目全部下载下来了，直接去看对应的markdown即可


``` python
import requests
import openpyxl
from openpyxl import load_workbook


def write_excel(a,b):
    wb = load_workbook(filename='牛客网.xlsx')
    ws = wb.active
    num = 1
    while 1:
        cell = ws.cell(row=num, column=1).value
        if cell:
            num = num +1
        else:
            row_num = num
            break
    ws.cell(row=row_num, column=1, value=str(a))
    ws.cell(row=row_num, column=2, value=str(b))
    wb.save('牛客网.xlsx')
def get_answer(id):
    url = "https://m.nowcoder.com/test/get-all-question?t=02436CC60E649584D5C4BBF57709E5CA&fm=android_app_2.21.3.3091&tid={}".format(id)
    print(url)
    headers = {
        "cookie": "这里需要填写网站对应的cookie",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36"
        }
    html = requests.get(url=url,headers=headers)
    json_response = html.json()
    question_list = json_response['data']['allQuestion']
    for question in question_list:
        print("="*20)
        print("题目：")
        topic = question['question']['content']
        print(topic)
        print("答案：")
        answer_list = question['question']['answer']
        for answer_id in answer_list:
            if answer_id["type"] == 1:
                answer = answer_id["content"]
                print(answer)
        write_excel(topic,answer)
        print("="*20)
    print("写入完毕！")
while True:
    id = input("请输入正在用该cookie刷题页面url里面的tid参数：") #tid的参数
    get_answer(id)



```
