# Python 使用 lambda 关键字创建匿名函数，JavaScript 使用 function 或 => 创建匿名函数。
# Python 的 lambda 函数不能包含函数体，表达式的值将作为返回值自动返回。而 JavaScript 中的匿名函数可以有函数体和 return 语句。

# 使用匿名函数，将数字列表的每一项映射为它的平方并打印新列表。

# js实现
# const numbers = [1, 2, 3, 4, 5];
# const squaredNumbers = numbers.map(number => number ** 2);
# console.log(squaredNumbers);

# py实现
numbers = [1,2,3,4,5]
squared_numbers = list(map(lambda number:number ** 2,numbers))
print(squared_numbers)