# token获取 + 自动签到
相信对这篇帖子感兴趣的都是学校里面有流海云印这个共享打印机吧~
众所周知，流海有一个签到功能，每天可以获得不等的鱼籽，最后这些鱼籽都可以进行订单抵扣，博主就一直手动签到，基本这几年，打印东西没充值过，哈哈哈。最近想的通过程序解决手动签到的麻烦，如有侵权或其他问题请联系我进行删除/关闭。
本次分享仅做测试学习交流使用，请勿非法使用！

文件夹下准备：pushplus_token.txt save_cookie.exe start_sign.exe
## 第一步：pushplus_token.txt 
如没有请手动创建，文件里面输入一行信息，即是你的pushplus公众号发给你的token，不要多输入无关信息
设置pushplus微信推送参考：https://www.pushplus.plus/push1.html

## 第二步：save_cookie.exe
点击运行，保存需要打卡的账号信息，可以多添加账号，只打卡一个账号添加账号后关闭软件即可！添加进去的账号一周有效，请于下周同一时候去重新打开这个软件更新账号信息，否则会打卡不上，详见pushplus给你的推送结果！同时文件夹下出现 cookie.json 文件，请勿删除！
*请单独下载修复版：https://wwrm.lanzoub.com/iCS4u0kizpod

## 第三步：start_sign.exe 
设置计划任务，放在服务器上，定时运行即可，每天一次即可！设置定时任务参考：https://blog.csdn.net/qq_43847263/article/details/111931598

### 补充：cookie.json
里面的参数有：

ID：手机号

token:密码

ua：UA标识

school_id：学校代码

第一次创建的cookie.json只需要你记住school_id参数即可，之后如果不想用save_cookie.exe更新token，那么可以用“token获取安卓版.apk”进行获取，最后编辑token文件替换旧token即可！

