# 生成一个包含 1 到 10 的平方的数的列表，然后过滤列表中的奇数。
# 生成一个包含 1 到 10 的平方数的字典，以数字作为键，平方数作为值，过滤字典中值大于等于5的键值对。

# 类似js中的const squaredNumbers = Array.from({length:10}, (_,i) => (i+1)**2);
squared_numbers = [x**2 for x in range(1,11)]
# 类似于js中的const filteredNumbers = squaredNumbers.filter(num => num % 2 === 0);
filter_numbers = [num for num in squared_numbers if num %2==0]
print(filter_numbers)  

squared_dict = {x:x**2 for x in range(1,11)}
print(squared_dict)
filter_dict = {key:value for key,value in squared_dict.items() if value<5}
print(filter_dict)