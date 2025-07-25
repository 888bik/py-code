import json

# json字符串转为Python字典
person = '{"name":"bik","age":18}'

dic = json.loads(person)

print(dic)

print(type(dic))

# python字典转为json字符串

s = {"name": "zkz", "age": 20}

jsonString = json.dumps(s)

print(jsonString)

print(type(jsonString))
