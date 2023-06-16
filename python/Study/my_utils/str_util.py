"""
字符串相关的工具模块
"""

def str_reverse(s):
    """
    将字符串反转
    :param s: 待反转字符串
    :return: 反转结果
    """
    return s[::-1]

def substr(s, x, y):
    """
    对字符串按索引进行切片
    :param s: 待切片字符串
    :param x: 开始索引
    :param y: 结束索引
    :return: 切片结果
    """

    return s[x:y]

if __name__ == '__main__':
    print(str_reverse("人生路漫漫"))
    print(substr("人生路漫漫", 1, 3))
