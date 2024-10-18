# 通过占位的形式，完成拼接
name = "Curry"
message = "hello %s" % name
print(message)

# 通过占位的形式，完成数字和字符串的拼接
class_num = 57
avg_salary = 16781.00
message = "第%d期，价格%f" % (class_num, avg_salary)
print(message)

# 宽度限制及精确小数点几位
num1 = 11
num2 = 11.345
print("数字11宽度限制5，结果是：%5d" % num1)
print("数字11宽度限制1，结果是：%1d" % num1)
print("数字11.345宽度限制7，小数精度2，结果是：%7.2f" % num2)
print("数字11.345宽度不限制，小数精度2，结果是：%.2f" % num2)

# 快速字符串格式化
# 语法：f"内容{变量}"
print(f"我是{name}，{class_num}，{num2}")