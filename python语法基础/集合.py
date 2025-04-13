# 集合是一个无序的唯一元素的集合，与 JavaScript 中的 Set 相同，常用语去重操作。

# 将文本中的水果按照空格拆分，去除重复项并对其进行排序。

# js实现
# const text = "apple banana cherry apple banana";
# const words = text.split(" ");
# const uniqueWords = [...new Set(words)];
# uniqueWords.sort();
# console.log(uniqueWords);

# py实现
text = "apple banana cherry apple banana"
words = text.split(" ")
# 创建集合
unique_words = set(words)
print(unique_words)
sorted_words = sorted(unique_words)
print(sorted_words)

# 添加元素
unique_words.add("orange")
print(unique_words)
# 检查大小
print(len(unique_words))
# 检查是否为空
print(len(unique_words) == 0)
# 删除元素 
unique_words.remove("apple")
print(unique_words)
# 清空集合
new_set = unique_words # 这里应该赋值的是引用
# print(new_set)
# new_set.clear() # 清除new_set也会将unique_words里的元素也一起删除
print(new_set)
# 检查成员是否存在
print("orange" in unique_words)
# 将集合转化为数组
new_list = list(unique_words)
print(new_list)
# 集合的并集
another_set = set({"orange","peach"})
print(unique_words.union(another_set))
# 集合的交集
print(unique_words.intersection(another_set))

