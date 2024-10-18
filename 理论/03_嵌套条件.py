if int(input("请输入你的身高（cm）:")) > 120:
    print("您的身高超过120cm，游玩需要买票10元。")
    print("但是，如果VIP级别大于3，可以免费")
    if int(input("请输入你的VIP等级（1-5）：")) > 3:
        print("VIP级别大于3，可以免费游玩。")
    else:
        print("Sorry，你需要买票10元。")
else:
    print("欢迎你，免费游玩。")