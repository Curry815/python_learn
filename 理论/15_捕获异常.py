try:
    f = open("E:/123.txt", "r", encoding="UTF-8")
except Exception as e:
    print("出现异常了")
    print(e)
    f = open("E:/面试技术/123.txt", "w", encoding="UTF-8")
else:
    print("哈哈，没有异常")
finally:
    f.close()