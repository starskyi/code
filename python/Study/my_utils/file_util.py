"""
文件处理相关模块
"""

def print_file_info(file_name):
    """
    读取文件内容并打印
    :param file_name: 文件名称
    :return: None
    """
    f = None
    try:
        f = open(file_name, "r", encoding="UTF-8")
        print(f.read())
    except Exception as e:
        print(f"出错了:{e}")
    finally:
        if f:
            f.close()


def append_to_file(file_name, data):
    """
    将数据追加到文件中
    :param file_name: 文件名称
    :param data: 追加的数据
    :return: None
    """
    f = open(file_name, "a", encoding="UTF-8")
    f.write(data)
    f.write("\n")
    f.close()

if __name__ == '__main__':
    print_file_info("D:/code/work.txt")
    append_to_file("D:/code/work.txt", "how are you")
