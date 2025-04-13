# 字典通常用于使用特定键存储和检索数据。Python 中的字典与 JavaScript 中的对象基本等价。
# 设计一个程序，使用字典存储和检索学生的个人信息。个人信息包括姓名、年龄和城市
# js实现
# let personalInfo = {};

# personalInfo.name = 'zsd',
# personalInfo.age = 18,
# personalInfo.city = '清远'

# console.log(personalInfo);

# py实现
person_info = {}
person_info2 = {"name":"zsd","age":18,"city":"清远"}

person_info["name"] = "zsd"
person_info["age"] = 18
person_info["city"] = "清远"


# 访问值
print(person_info)
print(person_info2)
print(person_info["name"])
print(person_info["age"])
print(person_info["city"])
# 访问值或默认值
print(person_info.get("abc","保密"))
# 更新
person_info["age"] = 20
print(person_info["age"])
# 合并和更新
newDict = {"height":1.88,"habit":"coding"}
person_info.update(newDict)
print(person_info)
# 删除键值对
del person_info2["city"]
print(person_info2)
# 检查键值对是否存在
print("name" in person_info)
# 获取所有键值对
print(person_info.keys())
# 获取所有值
print(person_info.values())
# 获取键值对数目
print(len(person_info))


# Python 中使用 {} 语法创建字典时，字典的 key 必须使用引号包裹。
# 此外，Python 还可以通过 dict() 来创建字典，并给字典设置初始键值对，这种方式不需要使用引号将 key 进行包裹。
dict1 = dict(a=1,b=2,c=3)
print(dict1)

# 在 Python 和 JavaScript 中，都可以使用 {} 创建一个空字典/对象。
# 在 Python 中，只能使用方括号（my_dict[key]）访问值，而 JavaScript 中，除了方括号外，还可以使用点运算符（myObj.key）访问值。