def check(num):
    if num <= 37.5:
        print(f"您的体温是：{num}度，体温正常请进！")
    else:
        print(f"您的体温是：{num}度，需要隔离！")

check(37.3)
check(39.3)