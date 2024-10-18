str = "itheima itcast boxuegu"

# 统计字符串内有多少个“it”字符
count = str.count("it")
print(count)

# 将字符串内的空格，全部替换为字符“|”
new_str = str.replace(" ", "|")
print(new_str)

# 按照“|”进行字符串分割，得到列表
new_str2 = new_str.split("|")
print(new_str2)
