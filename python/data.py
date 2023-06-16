from csv import reader, writer

with open("D:\\temp\\data.csv", "w") as fp:
    w = writer(fp)
    w.writerow(["日期", "销量"])
