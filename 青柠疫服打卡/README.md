## 青柠疫服每日打卡
#### 1.纯requests版本，避免了selenium等方式容易出现故障情况；
#### 2.基于ddddocr免费的验证码识别系统，避免了百度ocr等接口错误率高，收费等弊端；
#### 3.支持批量添加账号，一次获取UID,打卡时不再需要登录；
## 仓库下包含：
get_uid.py : 单独获取UID程序

daka.py : 打卡脚本
其中参数

    YXDM：学校代码
    请查看API接口获取： https://yqfkapi.zhxy.net/api/School/GetList?LX=1 
    
    position：中文地址，可以参考你以前的打卡地点
    API接口获取 ：https://yqfkapi.zhxy.net/api/ClockIn/GetClockList?yxdm={学校代码}&UID={你的UID}&UserType=1
    
    push_key：Pushdeer密钥，一个便携消息推送器
    下载地址|获取教程 ：https://www.pushdeer.com/official.html
