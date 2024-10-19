with open("E:/面试技术/word.txt", "r", encoding="UTF-8") as f:
    count = 0
    for line in f:
        count += line.count("itheima")
    print(f"单次出现的次数为：{count}")