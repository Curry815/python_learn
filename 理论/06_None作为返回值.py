# None的使用场景：
# 函数的返回值
# if判断
# 变量定义

def check_age(age):
    if age > 18:
        return "SUCCESS"
    return None

result = check_age(5)
if not result:
    print("未成年不可进入！")

name = None