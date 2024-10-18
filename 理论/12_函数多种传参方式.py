"""
1.位置参数
2.关键字参数
3.缺省参数（默认值）
4.不定长参数
"""
from tkinter.font import names


def user_info(name, age, gender):
    print(f"姓名是：{name}，年龄是：{age}，性别是：{gender}")
user_info("小明", 18, "男")
user_info(name="小红", age=16, gender="女")
# 缺省值要放在最后面
user_info("小兰", 20, gender="男")

# *号 参数类型是元组
def user_info(*args):
    print(f"参数类型{type(args)}，内容是：{args}")
user_info(1, 2, 3, "小明") # 参数类型<class 'tuple'>，内容是：(1, 2, 3, '小明')

# **号 参数类型是字典
def user_info(**args):
    print(f"参数类型{type(args)}，内容是：{args}")
user_info(name="小天", age=20, gender="男") # 参数类型<class 'dict'>，内容是：{'name': '小天', 'age': 20, 'gender': '男'}