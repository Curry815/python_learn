import time
import threading

def sing():
    while True:
        print("我在唱歌...")
        time.sleep(1)

def dance():
    while True:
        print("我在跳舞...")
        time.sleep(1)

if __name__ == '__main__':
    # 创建一个唱歌的线程
    sing_thread = threading.Thread(target=sing)
    # 创建一个跳舞的线程
    dance_thread = threading.Thread(target=dance)

    # 启动线程
    sing_thread.start()
    dance_thread.start()