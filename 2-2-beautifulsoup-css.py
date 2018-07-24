# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 14:05:59 2018

@author: LiJian
"""

from bs4 import BeautifulSoup

from urllib.request import urlopen

html=urlopen("https://morvanzhou.github.io/static/scraping/list.html").read().decode("utf-8")
print(html)

soup=BeautifulSoup(html,"html5lib")

month=soup.find_all("li",{"class":"month"})
for m in month:
    print(m.get_text())