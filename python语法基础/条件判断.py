score = 10
if score > 80:
  print("优秀")
elif score > 60 and score <80:
  print("及格")
elif score < 60:
  print("不及格")
else:
# 当代码块中不需要执行实际的逻辑时，为了让程序能正常运行，可以使用 pass 表示什么都不做，如：
  pass # 什么都不做
level = "及格" if score>=60 else "不及格"
print(level)

# Python if 语句中的条件周围不需要加圆括号，JavaScript 需要为条件添加圆括号。
# Python 使用冒号（:）表示条件结束，并使用 缩进 来表示代码块，JavaScript 直接使用 {} 表示代码块。
# Python 使用 elif 继续匹配判断条件，而 JavaScript 中使用 else if。

# Python 中判断一个值是否为空，可以使用 is None 、 is not None 、== None 和 != None 四种方式。

# Python 中没有 switch-case 语句。

# 逻辑运算符 
# js:&& || ! 
# python:and or not

# 等于,不等于
# js:===,!==
# python:==,!=

# 条件表达式
# js: let level = score >=60? "及格":"不及格"
# py: level = "及格" if score>=60 else "不及格"

