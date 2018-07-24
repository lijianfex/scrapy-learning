# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 13:20:12 2018

@author: LiJian
"""


from bs4 import BeautifulSoup
from urllib.request import urlopen

# if has Chinese, apply decode()
html = urlopen("https://morvanzhou.github.io/static/scraping/basic-structure.html").read().decode('utf-8')

soup = BeautifulSoup(html, "html5lib")
print(soup.h1)
print('\n', soup.p)

all_href = soup.find_all('a')
all_href = [l['href'] for l in all_href]
print('\n', all_href)