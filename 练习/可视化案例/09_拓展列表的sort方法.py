
# 准备列表
list = [["a", 33], ["b", 55], ["c", 11]]

# # 排序，基于带名函数
# def choose_sort_key(element):
#     return element[1]
# list.sort(key=choose_sort_key, reverse=True)

# 排序，基于lambda匿名函数
list.sort(key=lambda element: element[1], reverse=True)

print(list)