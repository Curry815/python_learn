str = "万过薪月，员序程马黑来，nohtyP学"

# 第一种方法
new_str = str[::-1][9:14]
print(new_str) # 学Python，来黑马程序员，月薪过万

# 第二种方法
new_str5 = str[5:10][::-1]
print(new_str5)

# 第三种方法
# 倒序字符串
# new_str = str[::-1]
# # print(new_str) # 学Python，来黑马程序员，月薪过万
# new_str2 = new_str.split("，")
# # print(new_str2) # ['学Python', '来黑马程序员', '月薪过万']
# new_str3 = new_str2[1].replace("来", "")
# print(new_str3)

new_str4 = str[::-1].split("，")[1].replace("来", "")
print(new_str4)






