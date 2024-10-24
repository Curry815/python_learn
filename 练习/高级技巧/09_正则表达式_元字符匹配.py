import re
s = "itheima @@python2 !!666 ##itcast3"

# 找出数字
result = re.findall('\d', s)
print(result) # ['2', '6', '6', '6', '3']

# 找出特殊字符
result2 = re.findall('\W', s)
print(result2) # [' ', '@', '@', ' ', '!', '!', ' ', '#', '#']

# 找出全部英文字母
result3 = re.findall('[a-zA-Z]', s)
print(result3) # ['i', 't', 'h', 'e', 'i', 'm', 'a', 'p', 'y', 't', 'h', 'o', 'n', 'i', 't', 'c', 'a', 's', 't']
