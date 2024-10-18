money = 5000000
name = None
name = input("请输入你的名字：")

# 查询余额函数
def check_money(isQuery):
    if isQuery:
        print("----------查询余额-------------")
    print(f"{name}，您好，您的账户余额还有：{money}元")

# 存款函数
def save_money(num):
    print("----------存款操作------------")
    global money
    money += num
    print(f"您存款{num}元成功")
    check_money(False)

# 取款函数
def take_money(num):
    print("----------取款操作-----------")
    global money
    money -= num
    print(f"您取款{num}元成功")
    check_money(False)

# 主菜单函数
def check_main():
    print("----------主菜单------------")
    print("查询余额\t[输入1]")
    print("存款\t[输入2]")
    print("取款\t[输入3]")
    print("退出\t[输入4]")
    return input("请输入您的选择：")

while True:
    type = check_main()
    if type == "1":
        check_money(True)
        continue
    elif type == "2":
        sum = int(input("请输入您要存款的金额："))
        save_money(sum)
        continue
    elif type == "3":
        sum = int(input("请输入您要取款的金额："))
        take_money(sum)
        continue
    else:
        print("欢迎下次光临！")
        break





