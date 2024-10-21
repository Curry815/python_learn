import json
# 列表转json
data = [{"name": "张大山", "age": 30}, {"name": "王大锤", "age": 28}, {"name": "小小胡", "age": 35}]
json_str = json.dumps(data, ensure_ascii=False)
print(type(json_str)) # <class 'str'>
print(json_str)
# 字典转json
d = {"name": "王大锤", "age": 28}
json_str_d = json.dumps(d, ensure_ascii=False)
print(type(json_str_d))
print(json_str_d)
# json转列表
s = '[{"name": "张大山", "age": 30}, {"name": "王大锤", "age": 28}, {"name": "小小胡", "age": 35}]'
l = json.loads(s)
print(type(l))
print(l)
# json转字典
s = '{"name": "王大锤", "age": 28}'
d = json.loads(s)
print(type(d))
print(d)