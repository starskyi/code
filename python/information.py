
info1 = ["课程名称：数据仓库与挖掘", "上课时间：星期五1-2节", "上课班级：（商）计算机2101", "上课人数：30"]
info2 = ["姓名：肖鹏江", "学号：20210206610118", "班级：（商）计算机201班"]

with open("D:\\temp\\information.txt", "w") as fp:
    for i in range(4):
        fp.write(info1[i] + "\t")
        if(i < 3):
            fp.write(info2[i] + "\n")