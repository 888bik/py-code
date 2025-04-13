gb = "8192MB"
print(gb[:-2])
int_tb = int(gb[:-2]) / 1024
print(f"该磁盘容量为:{int_tb}TB")
# Python 使用与类型同名的内置函数（如：str(some_value), bool(some_value)等）进行数据转换，JavaScript 使用以 parse 为前缀的内置函数。
# 在 Python 中，'8192MB' 这样的字符串无法直接转换为整数或浮点数，因为它值与这两种类型不兼容，而 JavaScript 可以通过 parseInt 转换为整数。
# Python 中可以使用字符串切片语法（[start:end]）获取字符串的子串。