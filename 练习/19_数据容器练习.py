"""
列表嵌套：有3个教室[[],[],[]]，8名讲师['A','B','C','D','E','F','G','H']，
        将8名讲师随机分配到3个教室中

幸运数字6：输入任意数字，如数字8，生成nums列表，元素值为1~8，
          从中选取幸运数字(能够被6整除)移动到新列表lucky，打印nums与lucky。
"""

import random
lecturers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
classrooms = [[], [], []]
for lecturer in lecturers:
    random_classroom = random.randint(0, 2)
    classrooms[random_classroom].append(lecturer)
print(classrooms) # 每次结果都不一样 [['C', 'D'], ['E', 'G'], ['A', 'B', 'F', 'H']]


num = int(input("请输入一个数字："))
nums = list(range(1, num + 1))
lucky = [i for i in nums if i % 6 == 0]
print(f"nums: {nums}") # nums: [1, 2, 3, 4, 5, 6, 7, 8]
print(f"lucky: {lucky}") # lucky: [6]
