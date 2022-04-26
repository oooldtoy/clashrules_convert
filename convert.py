import requests,yaml,os
import conf
def run(url_group_name):
    convert_dict = {}
    subscription_text = requests.get(conf.subscription_url).text
    subscription_dict = yaml.load(subscription_text,Loader=yaml.FullLoader)#yaml转dict
    subscription_proxies = subscription_dict['proxies']#获取proxies

    subscription_proxies_names = []
    for proxy in subscription_proxies:#获取proxy的name
        subscription_proxies_names.append(proxy['name'])

    proxy_groups_自动优选 = {'name':'自动选优','type':'url-test','proxies':subscription_proxies_names,'url': 'http://google.com/generate_204','interval':conf.interval}
    proxies_name_国外流量 = list.copy(subscription_proxies_names)
    proxies_name_国外流量.insert(0,'自动选优')
    proxies_name_国外流量.append('DIRECT')
    proxies_name_国外流量.append('REJECT')
    proxy_groups_国外流量 = {'name':'国外流量','type': 'select','proxies':proxies_name_国外流量}
    proxy_groups_conf = []
    for name in url_group_name:
        if name == '国外流量':#为了其他分组包含国外流量
            pass
        else:
            proxy_groups_conf.append({'name':name,'type':'select','proxies':['国外流量']+proxies_name_国外流量})
    proxy_groups = [proxy_groups_自动优选]+[proxy_groups_国外流量]+proxy_groups_conf

    def addgroup_(rules_list,rules_group):
        n = 0
        for i in rules_list:
            if 'IP-CIDR' in rules_list[n]:
                rules_list[n] = rules_list[n] + ',' + rules_group + ',no-resolve'
            else:
                rules_list[n] = rules_list[n] + ',' + rules_group
            n = n + 1
        return rules_list

    def addgroup(rules_group):#给规则添加规则组
        if conf.group_name[rules_group] == '':
            f = open('base_rules/'+rules_group+'.yaml',encoding='utf-8',mode='r')
            rules_text = f.read()
            rules_list = yaml.load(rules_text,Loader=yaml.FullLoader)
            f.close()
            return addgroup_(rules_list,rules_group)
        else:
            try:
                rules_text = requests.get(conf.group_name[rules_group]).text
            except:
                return '无法获取链接规则信息'
            f = open('base_rules/tmp.yaml',encoding='utf-8',mode='w')
            f.write(rules_text)
            f.close()
            f = open('base_rules/tmp.yaml', encoding='utf-8', mode='r')
            rules_list = []
            for i in range(conf.rulesline_max):
                a = f.readline()
                if a.startswith('DOMAIN') or a.startswith('IP-CIDR'):
                    rules_list.append(a.replace('\n', '').replace(',no-resolve', ''))
            f.close()
            return addgroup_(rules_list,rules_group)

    def yaml_list():#列出当前文件夹下的yaml文件
        a = os.listdir('base_rules')
        yamllist = []
        for i in a:
            if '.yaml' in i:
                yamllist.append(i.replace('.yaml', ''))
        return yamllist

    def rules_list():#整合rules
        yamllist = yaml_list()+['DIRECT']
        rules_list = []
        for name in url_group_name:
            if conf.group_name[name] != '':
                getrules = addgroup(name)
                if getrules == '无法获取链接规则信息':
                    print(name+getrules)
                else:
                    rules_list = rules_list+addgroup(name)
            elif name in yamllist:
                rules_list = rules_list + addgroup(name)
            else:
                print(name+' 未找到相关规则文件或链接')
        return rules_list+['MATCH,DIRECT']


    convert_dict['proxies'] = subscription_proxies
    convert_dict['proxy-groups'] = proxy_groups
    convert_dict['rules'] = rules_list()

    convert_yaml = yaml.dump(convert_dict,allow_unicode=True)#dict转换为yaml

    f = open('convert_rules/'+str(url_group_name)+'.yaml',encoding='utf-8',mode='w')
    f.write(convert_yaml)
    f.close()
if __name__=='__main__':
    run(['Telegram','Netflix','Steam','苹果服务','国外媒体','国外流量','广告','其他流量'])