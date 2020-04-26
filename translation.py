# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import json
import time
while True:
    promet = input("请输入翻译的内容(输入q! 退出程序)：")
    if promet == 'q!':
        break
    else:
        url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
        data = {}
        data['i'] = promet
        data['from'] = 'AUTO'
        data['to'] = 'AUTO'
        data['smartresult'] = 'dict'
        data['client'] = 'fanyideskweb'
        data['salt'] = '15877098747270'
        data['sign'] = 'e550f6070e9ecd4ed3efc6a384646697'
        data['ts'] = '1587709874727'
        data['bv'] = '70244e0061db49a9ee62d341c5fed82a'
        data['doctype'] = 'json'
        data['version'] = '2.1'
        data['keyfrom'] = 'fanyi.web'
        data['action'] = 'FY_BY_CLICKBUTTION'
        data = urllib.parse.urlencode(data).encode('utf-8')
        head = {}
        head[
            'User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'

        # response = urllib.request.urlopen(url, data, head)
        response = urllib.request.Request(url, data,headers=head)
        #response.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36')
        response = urllib.request.urlopen(response)
        html = response.read().decode('utf-8')
        target = json.loads(html)
        print("翻译结果：%s " % (target['translateResult'][0][0]['tgt']))
        time.sleep(3)
