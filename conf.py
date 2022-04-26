#订阅地址目前只支持clash
subscription_url = ''

#分组,每个分组值要么为空，要么为规则url，规则要符合clash规范
group_name = {'Youtube':'',
              'Telegram':'https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Telegram.list',
              'Netflix':'https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Netflix.list',
              'Steam':'',
              'microsoft':'https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Microsoft.list',
              'onedrive':'https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/OneDrive.list',
              '苹果服务':'',
              '国外媒体':'',
              '国外流量':'',
              '广告':'https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanEasyList.list',
              '其他流量':'',
              }

#规则最大行数
rulesline_max = 15000

#自动优选间隔，单位：秒
interval = 3600

#订阅地址填写 http://127.0.0.1:5000/clash_convert/Youtube,Telegram,Netflix,Steam,苹果服务,国外媒体,国外流量,广告,其他流量/
#clash_convert/ 后面的内容为需要产生分组的参数，分隔使用英文逗号。
#参数排在越前面优先级越高，建议规则数量较少的或高度自定义规则写在前面。
#顺序推荐：Youtube>Telegram>Netflix>Steam>苹果服务>国外媒体>国外流量>广告>其他流量
#url传递的规则组需要包含在group_name里面，否则不会产生该分组。