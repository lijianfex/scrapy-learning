# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 12:59:14 2018

@author: LiJian
"""
from urllib.request import urlopen

html=urlopen("https://morvanzhou.github.io/static/scraping/basic-structure.html").read().decode("utf-8")
print(html)

import re #导入正则表达式模块
reslut=re.findall(r"<title>(.+?)</title>",html)
#print("\nthe web page title is:",reslut[0])

reslut=re.findall(r"<p>(.*?)</p>",html,flags=re.DOTALL)
#print("\nPage paragraph is: ", reslut[0])

res = re.findall(r'href="(.*?)"', html)
print("\nAll links: ", res)