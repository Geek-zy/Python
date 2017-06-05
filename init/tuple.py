#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# tuple 元组
# tuple和list非常类似，但是tuple一旦初始化就不能修改，没有append()，insert()这样的方法，其他获取元素的方法和list是一样的，但不能赋值成另外的元素，不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。

data = ("张懿", "男", "25")
print(data)

# 空tuple
t = ()

# 因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，所以只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
t = (1,)

