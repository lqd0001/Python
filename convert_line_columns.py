import csv
# 读取.dat文件的第一行和第二行数据
with open('./postProcessing/surfaceElevationAnyName/0/surfaceElevation.dat', 'r') as f:
    lines = f.readlines()
    first_line = lines[0].strip().split()
    second_line = lines[1].strip().split()
# 写入到 CSV 文件
with open('Gauge.csv', 'w', newline='') as fw:
    writer = csv.writer(fw)
    for row in zip(first_line, second_line):
        writer.writerow(row)
