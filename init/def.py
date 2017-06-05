#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
1、abs(x)：返回一个整数或浮点数的绝对值，如果是复数，返回它的模。
2、all(iterable)：当iterable中所有元素都为True时（或者iterable为空），返回True。
3、any(iterable)：当iterable中有元素为True时，则返回True。如果iterable为空，返回False。
4、ascii(object)：类似于repr()，返回一个输入对象的可打印的字符串。
5、bin(x)：将整数x转化为一个二进制字符串。当x不是int对象时，x必须实现__index__()方法来返回一个整型数值。
6、bool(x)：将一个值转换成一个boolean类型的值，省略x将返回False。
7、bytearray()：bytearray的构造函数。bytearray类型是一个可变的整数序列（0<=整数<256），即字节数组，例如：
8、bytes()：字节对象（bytesobject）的构造函数。bytes是bytearray的不可变版本：
9、callable(object)：判断一个对象是否可调用，如果一个实例的类实现了call()方法，则它是可以调用的。
10、chr(i)：返回编码值i对应的字符（str类型），i的有效值为0到1114111。与ord()正好相反。
11、classmethod(function)：返回一个类方法。
12、compile()：编译一个源，返回一个代码对象，该代码对象可以用来作为exec()或者eval()的参数。
13、complex(re,im)：复数的构造函数，re为返回复数对象的实数部分，im为虚数部分。
14、delattr(object,name)：删除一个对象的属性，相当于delobject.name。
15、dict()：字典类型的构造函数。
16、dir()：返回一个包含了object所有属性的列表对象，如果没有参数，则包含当前作用域的所用属性。
17、divmod(a,b)：返回一个元组(a//b,a%b)。
18、enumerate(iterable,start=0)：返回一个可迭代的enumerateobject，对其使用next()得到的是包含索引和元素的tuple，通常用于同时遍历索引和元素：
19、eval()：执行一段代码，返回执行的结果。
20、exec()：也是执行一段代码，返回None。
21、filter(function,iterable)：过滤器，返回由使函数function返回True的iterable元素组成的迭代器。
22、float(x)：返回一个浮点型的对象，无参时返回0.0
23、format(value[,spec])：格式化一个值，当参数是一个自定义对象的时候，该对象需要实现__format__()方法。
24、frozenset()：frozenset的构造函数。顾名思义，frozenset是一种set类型，且不可改变（没有add、remove等方法）。
25、getattr(object,name)：获得对象的name属性，当该属性不存在的时候可以使用一个默认值作为返回值。
26、globals()：返回一个包含当前所有全局符号和对应值的字典。
27、hasattr(object,name)：判断对象是否有name属性。
28、hash(object)：返回对象的hash值，object必须是可哈希的。注意：所有不可变的内置类型都是hashable的，比如string，tuple；所有可变的内置类型都是unhashable的，比如list，dict（即没有__hash__()方法）。
29、help()：查看一个对象的帮助文档。
30、hex(x)：将一个整数转为小写的十六进制字符串（以’0x’开头），如果不是int对象，需要定义__index__()方法。
31、id()：返回一个对象的id身份，可以看作该对象的内存地址。
32、input()：读取一行输入并返回一个字符串。
33、int(x,base=10)：返回相应进制的int值。
34、isinstance(object,class)：判断对象object是不是类class或其派生类的实例。
35、issubclass(class,baseclass)：判断一个类是否是另一个类的子类。
36、iter()：返回一个可迭代的对象。
37、len()：返回一个长度值，与object中的__len__()有关。
38、list()：list的构造函数。
39、locals()：返回一个包含当前局部符号和对应值的字典，与globals()对应。
40、map(function,iterable)：映射函数，将iterable中的每个元素应用到function函数，返回由所有结果组成的迭代器。
41、max()：最大值。
42、min()：最小值。
43、memoryview(obj)：返回一个memoryview对象。
44、next(iterator)：产生下一个生成值，与__next__()有关。
45、object()：略。
46、oct(x)：将一个整数转为一个八进制字符串。如果不是int对象，需要定义__index__()方法。
47、open()：打开一个文件，返回对应的文件对象。
48、ord(c)：返回字符c的编码值，与chr(i)相反。
49、pow(x,y[,z])：pow(x,y)相当于x**y，pow(x,y,z)相当于pow(x,y)%z。
50、print()：打印输出。
51、property(fget=None,fset=None,fdel=None,doc=None)：函数property()的作用就是把类中的方法当作属性来访问。看下面的例子：
52、range(start,stop[,step])：返回一个序列。
53、repr(object)：将对象转化为可打印的字符串。
54、reversed()：倒序序列，对象需要实现__reversed__()方法。
55、round(number[,ndigits])：把浮点数转变成指定小数位数的数，ndigits默认为0。
56、set()：set的构造函数。
57、setattr(object,name,value)：为一个对象的name属性设置一个value值。
58、slice(start,stop[,step])：切片函数，分割一个可分割的对象，返回其中的一部分。
59、sorted()：排序。
60、staticmethod(function)：返回一个静态的方法。要知道，一个类的静态方法没有隐式的第一个self参数，因为静态方法是独立于实例对象的：
61、str()：字符串的构造函数。
62、sum()：求和。
63、super()：super()常用于继承中调用父类的方法。例如，类的继承中，通常需要调用父类的构造方法，以初始化父类部分，有两种方法能达到这个目的。
64、tuple()：元组的构造函数。
65、type()：返回一个对象的类型，返回值与object.__class__一样。
66、vars(object)：返回object中所有属性与对应值的字典。没有参数时作用和locals()一样。
67、zip()：zip函数接受一系列可迭代的对象作为参数，将对象中对应的元素打包成一个个tuple（元组）。
68、__import__()：通过import语句调用。
'''

def my_abs(x):

    if x > 0:
        return x

    else:
        return -x

print(my_abs(-3))

