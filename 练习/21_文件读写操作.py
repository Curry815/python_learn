"""
需求：
读取文件
将文件写出到bill_copy.txt文件作为备份
同时，将文件内标记为测试的数据行丢弃

实现思路：
open和r模式打开一个文件对象，并读取文件
open和w模式打开另一个文件对象，用于文件写出
for循环内容，判断是否是测试不是测试就write写出，是测试就continue跳过
将2个文件对象均close()
"""

# 打开文件得到文件对象，准备读取
f = open("E:/面试技术/bill.txt", "r", encoding="UTF-8")
# 打开文件得到文件对象，准备写入
f2 = open("E:/面试技术/bill_copy.txt", "w", encoding="UTF-8")
# for循环读取文件
for line in f:
    # 第一种方法
    line = line.strip()
    if line.split(",")[4] == "测试":
        continue
    f2.write(line)

    # 第二种方法
    # if "测试" not in line:
    #     f2.write(line)

f.close()
f2.close()