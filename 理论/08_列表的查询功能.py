list = ["python", "javascript", "vue"]
# 查询下标索引
index = list.index("python")
print(index)

# 修改特定下标索引的值
list[1] = "TypeScript"
print(list)

# 在指定下标位置插入新元素 insert
list.insert(1, "html")
print(list)

# 追加元素 append
list.append("css")
print(list)

# 追加多个元素 extend
list.extend([1, 2, 3])
print(list)

# 删除指定下标的元素 del 列表[下标] 或者 列表.pop(下标)
del list[2]
print(list)

result = list.pop(2)
print(list, result)

# 删除某元素在列表中第一个匹配项
list.remove("css")
print(list)

# 清空列表
list.clear()
print(list)

# 统计列表内某元素的数量
list = ["python", "javascript", "vue", "python"]
count = list.count("python")
print(count)

# 统计列表中全部的元素数量
count = len(list)
print(count)
