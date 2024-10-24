import socket

# 创建Socket对象
socket_server = socket.socket()
# 绑定ip地址和端口
socket_server.bind(("localhost", 8888))
# 监听端口
socket_server.listen(1)
# listen方法内接受一个参数，表示接受的连接数量
# 等待客户端连接
# result = socket_server.accept()
# conn = result[0] # 客户端和服务端的连接对象
# address = result[1] # 客户端的地址信息
conn, address = socket_server.accept()
# accept方法返回一个二元元组，第一个元素是客户端连接对象，第二个元素是客户端地址信息
# accept方法是阻塞方法，等待客户端的连接，如果没有连接，就卡在这一步不向下执行
print(f"接收到了客户端{address}的连接")

while True:
    # 接受客户端连接，要使用客户端和服务端的本次连接对象，而非socket_server对象
    data: str = conn.recv(1024).decode("UTF-8")
    # recv接受的参数是缓冲区大小，一般为1024，返回值是一个字节数组，即bytes对象，不是字符串，可以通过decode方法通过UTF-8编码转换为字符串对象
    print(f"客户端发送的消息为：{data}")
    # 发送回复消息
    msg = input("请输入你要和客户端回复的消息：")
    # encode可以将字符串编码为bytes字节数组对象
    if msg == 'exit':
        break
    conn.send(msg.encode("UTF-8"))
# 关闭连接
conn.close()
socket_server.close()