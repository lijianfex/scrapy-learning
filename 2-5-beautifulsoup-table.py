# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 15:39:54 2018

@author: LiJian
"""
from bs4 import BeautifulSoup
from urllib.request import urlopen

# if has Chinese, apply decode()
html = urlopen("https://morvanzhou.github.io/static/scraping/table.html").read().decode('utf-8')

soup = BeautifulSoup(html, 'html5lib')

# print with title
for item in soup.find("table", {"id": "course-list"}).children:
    print(item)

print("-------------------------")
# print without title
for item in soup.find("table", {"id": "course-list"}).tr.next_siblings:
    print(item)

print("-------------------------")
# navigate using next_sibling/previous_sibling
print(soup.find("img", {"src": "https://morvanzhou.github.io/static/img/course_cover/scraping.jpg"}
                ).parent.previous_sibling.get_text())

