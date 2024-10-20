def str_reverse(str):
    """
    字符串反转
    :param str:
    :return:
    """
    return str[::-1]

def substr(s, x, y):
    """
    字符串截取
    :param s: 字符串
    :param x: 切片下标开始
    :param y: 切片下标结束
    :return: 完成后的字符串
    """
    return s[x:y]

if __name__ == '__main__':
    print(str_reverse("字符串反转"))
    print(substr("字符串截取", 1, 3))
