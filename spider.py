# -*- coding: utf-8 -*-
import urllib.request

# a = urllib.request.urlopen("http://www.baidu.com")
# print(type(a))
# html = a.read()
# html = html.decode("utf-8")
# print(html)
resopen = urllib.request.urlopen("http://placekitten.com/g/500/500")
cat_img = resopen.read()
with open('cat_500_600.jpg','wb') as f:
    f.write(cat_img)