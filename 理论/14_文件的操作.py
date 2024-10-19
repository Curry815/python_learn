# 打开文件
import time

# f = open("E:/面试技术/面试所需的技术.md", "r", encoding="UTF-8")
# print(type(f)) # <class '_io.TextIOWrapper'>

# 读取文件 read()
# print(f"读取10个字节：{f.read(10)}")
# print(f"read方法读取全部内容的是：{f.read()}")

# 读取文件 readLines()
# lines = f.readlines() # 读取文件的全部行，封装到列表中
# print(f"lines对象的类型：{type(lines)}") # <class 'list'>
# print(f"lines对象的内容是：{lines}") # ['图像数据可视化标注工具开发\n', 'Canvas 2d绘图\n', '动画、协议、安全...

# 读取文件 readline() 一次只能读取一行
# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()
# print(f"第一行数据：{line1}")
# print(f"第二行数据：{line2}")
# print(f"第三行数据：{line3}")

# # for循环读取文件
# for line in f:
#     print(f"每一行数据是: {line}")
#
# # 关闭文件
# f.close()

# # with open 语法 读取完文件之后自动关闭文件
# with open("E:/面试技术/面试所需的技术.md", "r", encoding="UTF-8") as f:
#     for line in f:
#         print(f"每一行数据是：{line}")


# 写入文件 write() 不存在文件时，创建文件
# f = open("E:/面试技术/test.txt", "w", encoding="UTF-8")
# f.write("Hello")
# f.flush() # 刷新缓冲区，写入硬盘
# f.close() # 关闭文件，内置flush函数

# 存在文件，会覆盖掉之前的内容
# f = open("E:/面试技术/test.txt", "w", encoding="UTF-8")
# f.write("Hello!!!!")
# f.close()

# f = open("E:/面试技术/test2.txt", "a", encoding="UTF-8")
# f.write("Hello")
# f.flush() # 刷新缓冲区，写入硬盘
# f.close() # 关闭文件，内置flush函数

f = open("E:/面试技术/test2.txt", "a", encoding="UTF-8")
f.write("\nworld")
f.close() # 关闭文件，内置flush函数

