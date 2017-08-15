#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

Day = {'1':'甲', '2':'乙', '3':'丙', '4':'丁', '5':'戊', '6':'己', '7':'庚', '8':'辛', '9':'壬', '10':'癸'}
Ear = {'1':'寅', '2':'卯', '3':'辰', '4':'巳', '5':'午', '6':'未', '7':'申', '8':'酉', '9':'戌', '10':'亥', '11':'子', '12':'丑'}
Zod = {'1':'鼠', '2':'牛', '3':'虎', '4':'兔', '5':'龙', '6':'蛇', '7':'马', '8':'羊', '9':'猴', '10':'鸡', '11':'狗', '0':'猪'}

def Stock(year):
    
    # 如果是公元前需要减一年，因为是负数，所以加一
    if year < 0:
        year = year + 1

    # 天干算法 ==> 年份个位 - 3，个位小于等于 3 借 10
    day = (year % 10) - 3
    if day <= 0:
        day = 10 + day

    # 地支算法 ==> 年份 + 7 和 12 取余，余数为 0，则等于 12
    ear = (year + 7) % 12
    if ear == 0:
        ear = 12

    return Day[str(day)] + Ear[str(ear)]

def Zodiac(year):
    
    # 年份数 + 9 和12 取余
    if year > 0:
        zod = (year + 9) % 12
    
    # 公元前的年份要 + 1 之后再 + 9 再和12 取余
    else:
        zod = (year + 1 + 9) % 12

    return Zod[str(zod)]

import re
import os

os.system('clear')
year = input("\n * 请输入年份: ")

# 判断用户输入是否是 '-816-201' 这样的字符串
data = list(year)
data = '-' in data[1:]

# 判断用户输入是否是 0 - 9 的数字
# 判断用户输入是否超过 5 位字符串 包括 '-'
# 判断用户输入是否是 空,即直接敲回车
if (not re.match(r'^[-?0-9]{1,5}$', year)) or data == True:
    os.system('clear')
    print('\n* 年份输入有误,请重新输入! 范围: -9999 ~ 99999\n')

else:
    year = int(year)
    stock  = Stock(year)
    zodiac = Zodiac(year)
    
    if year > 0:
        os.system('clear')
        print('\n * 公元 %d 年对应天干地支纪年法是: %s%s 年\n' % (year, stock, zodiac))

    elif year < 0:
        os.system('clear')
        print('\n * 公元前 %d 年对应天干地支纪年法是: %s%s 年\n' % (abs(year), stock, zodiac))

    # 判断用户输入是否是 0
    else:
        os.system('clear')
        print('\n* 年份输入有误,请重新输入! 范围: -9999 ~ 99999\n')

