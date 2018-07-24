# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 16:22:04 2018
多进程
@author: LiJian
"""
from urllib.request import urlopen, urljoin
from bs4 import BeautifulSoup
import multiprocessing as mp
import re
import time

base_url = 'https://morvanzhou.github.io/'
 # base_url = "http://127.0.0.1:4000/"

def crawl(url):
    respones=urlopen(url)
    time.sleep(0.1)
    return respones.read().decode("utf-8")

def parse(html):
    soup=BeautifulSoup(html,"html5lib")
    urls=soup.find_all('a',{"href":re.compile('^/.+?/$')})    
    title=soup.find('h1').get_text().strip()    
    page_urls = set([urljoin(base_url, url['href']) for url in urls])   
    url = soup.find('meta', {'property': "og:url"})['content']   
    return title,page_urls,url

if __name__ == '__main__':
    
    if base_url != "http://127.0.0.1:4000/":
        restricted_crawl = True
    else:
        restricted_crawl = False
    
    unseen=set([base_url,])
    seen=set()
    
    pool=mp.Pool(4)
    count,t1=1,time.time()
    
    
    while len(unseen)!=0:
        if restricted_crawl and len(seen) > 20:
            break
        print("多进程爬取中........")
        crawl_jobs=[pool.apply_async(crawl, args=(url,)) for url in unseen]
        htmls=[j.get() for j in crawl_jobs]
        htmls=[h for h in htmls if h is not None]
        
        parse_jobs = [pool.apply_async(parse, args=(html,)) for html in htmls]
        results = [j.get() for j in parse_jobs]
        print("多进程分析网页........")
        
        seen.update(unseen)
        unseen.clear()        
        
        for title, page_urls, url in results:
            print(count, title, url)
            count += 1
            unseen.update(page_urls - seen)

    print('Total time: %.1f s' % (time.time()-t1, ))        
        
        
        
        
        
        
        
        
        
        
    