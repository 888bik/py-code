import re

# str = "hello what is your name?"
str = "你好python蟒蛇2025"
# findall表示查找所有,并返回list
# .表示匹配除了换行符以外的所有字符
res1 = re.findall(".", str)

# \w表示匹配字母,数字和下划线
res2 = re.findall(r"\w", str)

# d表示匹配一个数字,d+表示匹配一个或者多个数字
res3 = re.findall(r"\d+", str)


# search表示匹配第一个结果并返回,如果匹配不上则返回None
res4 = re.search(r"\d", str)


# finditer跟findall差不多,只不过finditer返回的是迭代器
res5 = re.finditer(r"\d", str)
# for s in res5:
# print(s.group())

# compile
regex = re.compile(r"\d+")


res6 = regex.search(str)
# print(res6.group())

str2 = """<div class='西游记'><span id='10010'>中国联通</span></div>
<div class='水浒传'><span id='10011'>中国电信</span></div>
<div class='红楼梦'><span id='10012'>中国移动</span></div>"""

regex1 = re.compile(
    r"<div class='(?P<title>.*?)'><span id='(?P<id>\d+)'>(?P<name>.*?)</span></div>", re.S)
res7 = regex1.finditer(str2)

# print(res7.group())
# print(res7.group("title"))
# print(res7.group("id"))
# print(res7.group("name"))

for res in res7:
    print(res.group("title"),res.group("id"),res.group("name"))

