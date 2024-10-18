import random
num = random.randint(1, 100)

# 判断循环是否继续的标志
flag = True
# 计数共猜测多少次
count = 0

while flag:
    guess_num = int(input("请输入你猜测的数字："))
    count += 1
    if guess_num == num:
        print("你猜对了")
        flag = False
    else:
        if guess_num > num:
            print("你猜大了")
        else:
            print("你猜小了")
