# -*- coding: utf-8 -*-
import urllib.request
import random
iplist =['192.168.0.3:80','45.56.97.56:99']
url = 'http://www.whatismyip.com.tw'
proxy_support = urllib.request.ProxyHandler({'http': random.choice(iplist)})
opener = urllib.request.build_opener(proxy_support)
opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36')]
urllib.request.install_opener(opener)
response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')
print(html)

