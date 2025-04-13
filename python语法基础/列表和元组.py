# 在 Python 中，数组被称之为列表，用于存储多个连续的值。
# 创建
names = []
# 添加
names.append("张三")
names.append("李四")
names.append("王五")
names.append("赵六")
# 访问
print(names) 
print(names[2])
# 获取长度
print(len(names))
# 切片
print(names[1:4])
# 连接
address = ["广州","北京","上海","深圳"]
print(names + address)
# 复制
names2 = names.copy();
print(names2)
# 反转
names.reverse()
print(names)
# 删除
del names[1]
print(names)
# 求最大值和最小值
print(max(names))
print(min(names))
# 求和
# print(sum(names))
# 转换为元组
print(tuple(names))
# 元组可以理解为只读的数组，它在创建时确定元素个数和元素的值，一旦创建就不能被修改。



