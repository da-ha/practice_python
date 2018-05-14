from bs4 import BeautifulSoup
import urllib.request as req
 
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = "https://www.nikkei.com/markets/kabu/"
 
# urlopen()でデータを取得
res = req.urlopen(url)
 
# BeautifulSoup()で解析
soup = BeautifulSoup(res, 'html.parser')
 
# 任意のデータを抽出
title1 = soup.find("span").string
print("title = ", title1)
 
