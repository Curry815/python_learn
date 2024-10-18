tp = ("周杰伦", 11, ["football", "music"])

# 查询年龄所在的下标位置
index = tp.index(11)
print(index)

# 查询学生的姓名
print(tp[0])

# del tp[2][0] 或者
tp[2].remove("football")
# 删除学生爱好中的football
print(tp)

# 增加爱好：coding到爱好list内
tp[2].append("coding")
print(tp)