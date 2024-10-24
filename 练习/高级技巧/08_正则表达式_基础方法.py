import re
s = "1python haha python python"
# match 从头匹配
# result = re.match("python", s)
# print(result.span()) # (0, 6)
# print(result.group()) # python
# result2 = re.match("1python", s)
# print(result2) # None

# search搜索匹配
result3 = re.search("python", s)
print(result3.span()) # (1, 7)
print(result3.group()) # python

# findall 搜索全部匹配
result4 = re.findall("python", s)
print(result4) # ['python', 'python', 'python']

r = '^[0-9][0-9]{4,10}$'
s1 = "0123456789"
print(re.findall(r, s1))

r2 = r'^[\w-]+(\.[\w-]+)*@(qq|163|gmail)(\.[\w-]+)$'
s2 = "abc.egs@qq.com"
print(re.findall(r2, s2)) # [('.egs', 'qq', '.com')]
