import urllib.request
from bs4 import BeautifulSoup
import ssl

ssl._create_default_https_context = ssl._create_unverified_context #SSL証明書が正しくない場合にはエラーとなる。以下を追加することで、対応できる。
url = "https://s.tabelog.com/tokyo/A1301/A130101/13218240/?svd=20180513&svt=1900&svps=2&default_yoyaku_condition=1"
headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
        }

request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
#html = response.read().decode('utf-8')
soup = BeautifulSoup(response, "html.parser")
#b = soup.find_all("b")
elems = soup.select('.class')
value = ""
print(elems)

for tag in elems:
  print(tag.value)
#      string_ = tag.get("class")
#      print(string_)
#      print(tag.string_)
#      for t in string_
#      if t in "rdheader-rating__score-val":
#        value = tag.string
#        break
              # 摘出したclassの文字列にmkc-stock_pricesと設定されているかを調べます
#      if "rdheader-rating__score-val-dtl" in string_:
            # mkc-stock_pricesが設定されているのでtagで囲まれた文字列を.stringであぶり出します
#            value = tag.string
            # 摘出が完了したのでfor分を抜けます
print("お店の評価は：" + str(value))

