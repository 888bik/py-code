# 函数用于对代码逻辑的封装和隔离，在 Python 和 JavaScript 中，函数都被视作一等公民。

# 编写一个打招呼的函数，将传入的个人信息（姓名、年龄、性别）格式化后打印。

def greet(name,age,gender="保密"):
  print(f"你好,我是{name},今年{age}岁,性别{gender}")

greet("张三",19,"男")# 传入位置参数
greet(age=22,name="李四",gender="男") # 传入关键字参数
greet("翠花",18)

# Python 使用 def 关键字定义函数，JavaScript 使用 function 关键字定义函数。
# Python 使用冒号 : 和缩进表示函数体，JavaScript 使用花括号表示函数体。
# Python 中，除默认值参数之外（如上面的 gender 参数），函数的每个参数都是必传的，否则会出现语法错误。而在 JavaScript 中未传递的参数默认值为 undefined。
# 在 Python 中，按照顺序传入的参数叫做 位置参数 ，必须严格按照形参定义顺序传入。此外，还可以使用 key=value 的形式向函数传入关键字参数，关键字参数的顺序不必与形参顺序保持一致，位置参数和关键字参数可以一起使用，但 必须保证调用函数时提供了所有必要参数 。
# Python 中，可以使用 my_fn(*[p1, p2, ...]) 的形式传入位置参数，与 JavaScript 中的 myFn(...[p1, p2, ...]) 类似。