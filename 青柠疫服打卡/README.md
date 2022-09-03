## 青柠疫服每日打卡

```json
   // 本脚本仅做代码交流学习使用，测试时请根据身体真实情况填写信息，请勿为疫情防控造成不必要的麻烦，否则法律责任自负！
```


##### 1.纯requests版本，避免了selenium等方式容易出现故障情况；
##### 2.基于ddddocr免费的验证码识别系统，避免了百度ocr等接口错误率高，收费等弊端；
##### 3.支持批量添加账号，一次获取UID,打卡时不再需要登录；
## 仓库下包含：
get_uid.py : 单独获取UID程序

daka.py : 打卡脚本

青柠打卡账号.csv ： 需要打卡多账号按格式依次往下填写即可，英文逗号隔开stu_name,stu_uid,push_key,position（姓名,UID,Pushdeer密钥,中文地址）

其中参数

    YXDM：学校代码
    请查看API接口获取： https://yqfkapi.zhxy.net/api/School/GetList?LX=1 
    
    position：中文地址，可以参考你以前的打卡地点
    API接口获取 ：https://yqfkapi.zhxy.net/api/ClockIn/GetClockList?yxdm={学校代码}&UID={你的UID}&UserType=1
    
    push_key：Pushdeer密钥，一个便携消息推送器
    下载地址|获取教程 ：https://www.pushdeer.com/official.html

