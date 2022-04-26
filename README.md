# clashrules_convert

clash自定义规则转换工具

使用方法：

1.在conf.py的subscription_url中填入订阅链接地址（目前只支持clash订阅地址）

2.在conf.py的group_name中自定义规则组名称

3.运行web_server.py

4.订阅地址：http://xxx.xxx.xxx.xxx:5000/clash_convert/Youtube,Telegram,Netflix,Steam,苹果服务,国外媒体,国外流量,广告,其他流量/

注：
“/clash_convert/Youtube,Telegram,Netflix,Steam,苹果服务,国外媒体,国外流量,广告,其他流量/” 为自定义规则的规则组，可自定义填写；每个规则组用英文逗号隔开；规则组需要包含在conf.py的group_name中；自定义规则组填写顺序为实际生成转换规则的顺序。

填坑：

1.将原订阅地址作为参数加入转换订阅地址中

2.兼容其他订阅

3.前端

