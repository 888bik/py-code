name = "bik"
msg = "hello"

# 获取长度
print(len(msg))
# 拼接
print(msg + name)
# 截取,切片
print(msg[2:4])
# 查找
print(msg.index("el"))# 找到则返回第一个找到的值的索引
print(msg.find("el"))# 如果找不到则返回-1
# 替换
print(msg.replace("hello","hi bik"))
# 分割
print(msg.split(","))
# 大小写转换
print(msg.upper())  
print(msg.lower())
# 反转
print(msg[::-1])
# 统计子串出现次数
res = msg + name + "hello zsd"
print(res.count("hello"))
# 是否以指定字符开头
print(msg.startswith("h"))
# 是否以指定字符结尾
print(msg.endswith("abc"))
# 删除两端的空白字符
print(res.strip())
# 按指定宽度居中对齐
print(msg.center(2))
# 第一个单词首字母大写
print(msg.capitalize())
# 每个单词首字母大写
print(res.title())