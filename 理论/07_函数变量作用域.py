# num = 200
# def testA():
#     print(f"testA---{num}")
# def testB():
#     num = 500
#     print(f"testB---{num}")
# testA()
# testB()


num = 200
def testA():
    print(f"testA---{num}")
def testB():
    global num # global设置内部定义的变量为全局变量
    num = 500
    print(f"testB---{num}")
testA() # 200
testB() # 500
print(num) # 500