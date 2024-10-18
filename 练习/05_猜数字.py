"""
需求：定义一个数字（1~10，随机产生），通过3次判断来猜出数字

要求：
    1.数字随机产生，范围1~10
    2.有3次机会猜测数字，通过3层嵌套判断实现
    3.每次猜不中，会提示大了或小了
"""

import random
num = random.randint(1,10)

guess_num = int(input("请输入你要猜测的数字是："))
if guess_num == num:
    print("哇塞，第一次就猜对了")
else:
    if guess_num > num:
        print("你猜大了")
    else:
        print("你猜小了")

    guess_num = int(input("再次输入你要猜测的数字是："))
    if guess_num == num:
        print("哇塞，第二次就猜对了")
    else:
        if guess_num > num:
            print("你猜大了")
        else:
            print("你猜小了")

        guess_num = int(input("最后一次输入你要猜测的数字是："))
        if guess_num == num:
            print("哇塞，第三次就猜对了")
        else:
            print("三次机会都用完了，没有猜中")