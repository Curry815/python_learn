list = [1, 2, 3, 4, 5]
result = list[1:4] # 下标1开始，下标4（不含）结束，步长1
print(result) # [2, 3, 4]

my_tuple = (1, 2, 3, 4, 5)
new_tuple = my_tuple[:]	# 从头开始，到最后结束，步长1
print(new_tuple)		# 结果：(1, 2, 3, 4, 5)

my_list = [1, 2, 3, 4, 5]
new_list = my_list[::2]		# 从头开始，到最后结束，步长2
print(new_list)		# 结果：[1, 3, 5]

my_str = "12345"
new_str = my_str[:4:2]	# 从头开始，到下标4（不含）结束，步长2
print(new_str) # 结果："13"

my_str = "12345"
new_str = my_str[::-1]	# 从头（最后）开始，到尾结束，步长-1（倒序）
print(new_str)		# 结果："54321"

my_list = [1, 2, 3, 4, 5]
new_list = my_list[3:1:-1]	# 从下标3开始，到下标1（不含）结束，步长-1（倒序）
print(new_list)		# 结果：[4, 3]

my_tuple = (1, 2, 3, 4, 5)
new_tuple = my_tuple[:1:-2] 	# 从头（最后）开始，到下标1(不含)结束，步长-2（倒序）
print(new_tuple)		# 结果：(5, 3)




