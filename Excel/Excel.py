#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import xlwt
import xlrd


# 写入Excel
def write():
    
    # 创建一个工作簿
    workbook = xlwt.Workbook('main')

    # 创建工作表
    worksheet  = workbook.add_sheet('sheet')
    worksheet1 = workbook.add_sheet('sheet1')
    worksheet2 = workbook.add_sheet('sheet2')

    # 写入单条数据
    # write() 参数 x, y, z 分别代表行、列、数据
    worksheet.write(0, 1, 'Nice')

    # 写入多条数据
    # 创建一个二维数组
    data = [[1, 2, 3, 4], [5, 6, 7, 8]]

    # 第一种方法，使用计数器循环写入
    for x in range(len(data)):
        for y in range(len(data[x])):
            worksheet1.write(x, y, data[x][y])

    # 第二种方法，使用迭代器遍历写入，推荐第一种
    i = 0
    for Xdata in data:
        j = 0
        for Ydata in Xdata:
            worksheet2.write(i, j, Ydata)
            j += 1

        i += 1

    # 保存到磁盘，路径+文件名+后缀名
    workbook.save('main.xlsx')


# 读取Excel
def read():

    # 打开 Excel 文件，路径+文件名+后缀名
    workbook = xlrd.open_workbook('main.xlsx')

    # 获取所有的工作表
    worksheet = workbook.sheets()

    # 获取工作表数目
    nums = len(worksheet)
    print(nums)

    # 获取工作表
    # 第一种方法，迭代输出
    for sheet in worksheet:
        print(sheet)

    # 第二种方法，计数器输出
    for num in range(nums):
        sheet = worksheet[num]
        print(sheet)

    # 第三种方法，根据工作表名称获取
    sheet = workbook.sheet_by_name('sheet1')
    
    # 获取工作表相关信息，数据有几行、几列
    x = sheet.nrows
    y = sheet.ncols
    print("* 当前 Excel 的工作表有 %d 行 %d 列" % (x, y))

    # 获取每行数据，计数器输出每行数据
    for i in range(x):
        row_data = sheet.row_values(i)
        print(row_data)

    # 获取独立单元格数据
    # 单元格获取
    cell = sheet.cell(0, 0).value
    print(cell)

    # 索引获取
    index = sheet.row(0)[0].value
    print(index)


write()
read()

