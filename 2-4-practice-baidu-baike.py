# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 14:27:13 2018

@author: LiJian
"""

from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random


base_url = "https://baike.baidu.com"
his = ["/item/%E8%B5%B5%E4%B8%BD%E9%A2%96"]

for i in range(20):
    # dealing with Chinese symbols
    url = base_url + his[-1]

    html = urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html, 'html5lib')
    print(i, soup.find('h1').get_text(), '    url: ', his[-1])

    # find valid urls
    sub_urls = soup.find_all("a", {"target": "_blank", "href": re.compile("/item/(%.{2})+$")})

    if len(sub_urls) != 0:
        his.append(random.sample(sub_urls, 1)[0]['href'])
    else:
        # no valid sub link found
        his.pop()