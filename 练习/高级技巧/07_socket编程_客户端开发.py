import socket

# 创建Socket对象
socket_client = socket.socket()
# 连接到服务器
socket_client.connect(("localhost", 8888))

while True:
    send_msg = input("请输入要发送给服务端的消息：")
    # encode可以将字符串编码为bytes字节数组对象
    if send_msg == 'exit':
        break
    socket_client.send(send_msg.encode("UTF-8"))

    recv_data = socket_client.recv(1024)
    print("服务端回复消息是：", recv_data.decode("UTF-8"))

# 关闭连接
socket_client.close()

