num = 10

if int(input("请输入第一次猜想的数字：")) == num:
    print("恭喜你，第一次就猜对了")
elif int(input("不对，再猜一次：")) == num:
    print("猜对了")
elif int(input("不对，再猜最后一次：")) == num:
    print("恭喜你，最后一次机会，你猜对了")
else:
    print("Sorry，全部猜错了，我想的是：%d" % num)
