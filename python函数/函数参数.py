# 使用 *args 获取传入的全部位置参数，类型为元组。使用 **kwargs 获取传入的全部关键字参数，类型为字典。
def greet(name,age,gender="保密",*args,**kwargs):
  print(f"你好,我是{name},今年{age}岁,性别{gender}")
  print(args)
  print(kwargs)

greet("张三",19,"男","hello",a=1,b=2)# 传入位置参数
greet(age=22,name="李四",gender="男") # 传入关键字参数
greet("翠花",18)

# Python 也可以使用 ** 展开一个字典
my_dict = {"name":"bik","age":19}
greet(**my_dict)
