# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 18:42:04 2018

@author: LiJian
"""

from bs4 import BeautifulSoup
import requests
import os
os.makedirs('./img/', exist_ok=True)

URL = "http://www.win4000.com/zt/xingganmeinv.html"

html = requests.get(URL).text
soup = BeautifulSoup(html, 'html.parser')
img_ul = soup.find_all('ul', {"class": "clearfix"})

i=0
for ul in img_ul:
    imgs = ul.find_all('img')
    for img in imgs:
        url = img['src']
        r = requests.get(url, stream=True)
        i+=1
        image_name = "Other"+str(i)+".jpg"
        with open('./img/%s' % image_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=128):
                f.write(chunk)
        print('Saved %s' % image_name)
            
            
            
            
            
            
            
            
            
            
            