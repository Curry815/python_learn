height = int(input("请输入你的身高（cm）:"))
vip_level = int(input("请输入你的VIP等级（1-5）："))

if height > 120:
    print("您的身高超过120cm，游玩需要买票10元。")
elif vip_level > 3:
    print("VIP级别大于3，可以免费游玩。")
else:
    print("不好意思，条件不满足，需要买票10元。")

print("祝您游玩愉快。")