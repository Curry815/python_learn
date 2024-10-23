"""
装饰器其实也是一种闭包，其功能就是在不破坏目标函数原有的代码和功能的前提下，为目标函数增加新功能。
"""
# def outer(func):
#     def inner():
#         print("我要睡觉了")
#         func()
#         print("我起床了")
#
#     return inner
#
# def sleep():
#     import random
#     import time
#     print("睡眠中....")
#     time.sleep(random.randint(1, 5))
#
# fn = outer(sleep)
# fn()

# @outer 语法糖
def outer(func):
    def inner():
        print("我要睡觉了")
        func()
        print("我起床了")

    return inner

@outer
def sleep():
    import random
    import time
    print("睡眠中....")
    time.sleep(random.randint(1, 5))

sleep()