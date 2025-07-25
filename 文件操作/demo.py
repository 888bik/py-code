# f = open("test.txt", mode="r", encoding="utf-8")
# content = f.read()
# f.close()

# print(content)


# 另一种写法,好处是不用手动关闭f
with open("test.txt", mode="r", encoding="utf-8") as f:
    for line in f:
        print(line)
