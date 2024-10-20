from idlelib.iomenu import encoding


def print_file_info(file_path):
    """
    打印文件信息
    :param file_path: 文件路径
    :return: None
    """
    f = None
    try:
        f = open(file_path, "r", encoding="UTF-8")
        content = f.read()
        print("文件内容如下：")
        print(content)
    except Exception as e:
        print(f"程序出现异常：{e}")
    finally:
        if f: # f有可能是异常
            f.close()


def append_to_file(file_path, data):
    """
    追加内容到文件
    :param file_path: 文件路径
    :param content: 内容
    :return: None
    """
    f = open(file_path, "a", encoding="UTF-8")
    f.write(data)
    f.write("\n")
    f.close()

if __name__ == '__main__':
    # print_file_info("E:/面试技术/bill.txt")
    append_to_file("E:/面试技术/bill.txt", "是否有内容追加")
