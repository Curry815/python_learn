"""
1.函数作为参数传递  可以重复使用
2.lambda匿名函数  临时使用一次
    语法：lambda 传入参数: 函数体（一行代码）
"""

def test_func(compute):
    result = compute(1, 2)
    print(result)

def add(x, y):
    return x + y

test_func(add) # 3
test_func(lambda x, y: x + y) # 3