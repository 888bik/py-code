from bs4 import BeautifulSoup

import requests

url = "https://news.ycombinator.com/"

response = requests.get(url)

# 把要解析的东西传递给BeautifulSoup
# 第一个参数是要解析的东西,第二个参数是使用什么解析器来解析内容,常见的有:html.parser ,lxml
soup = BeautifulSoup(response.text, "lxml")

# 第一种方式是用find查找元素标签,find表示找到第一个标签,并返回是element元素
res1 = soup.findAll("span", attrs={"class": "titleline"})
for res in res1:
    print(res.text)

res2 = soup.select(".titleline > a")
for href in res2:
    print(href.get("href"))

res3 = soup.select_one("title")
print("title:", res3.text)
