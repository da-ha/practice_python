#coding: utf-8
from bs4 import BeautifulSoup
from datetime import datetime

#変数htmlには上記のHTMLがstrで代入されているとします。
soup = BeautifulSoup(html)

#変数title, timestamp, author, author_link, bodyにそれぞれタイトル、投稿日時、著者、著者のリンク、記事本文が代入されます。
title = soup.h1.find(text=True)
timestamp = soup.find(id='container').find(class_='timestamp').find(text=True)
author = soup.find(id='articleInfo').find(class_='author').find('a').find(text=True)
author_link = soup.find(id='articleInfo').find(class_='author').find('a').get('href')
body = soup.find(id='articleText').find(text=True)



<html>
  <head>
    <meta charset='utf-8' />
  </head>
  <body>
    <h1>クローリングとスクレイピング</h1>
    <div id="articleInfo">
      <p>
        <span class="timestamp">2014-2-11 14:33:31</span>
        <span class="author"><a href="https://github.com/KaoruNasuno">KaoruNasuno</a></span>
      </p>
    </div>
    <div id="articleText">
      本節では、ウェブサイトのクローリングとスクレイピングについて説明します。。。  

    </div>
  </body>
</html>