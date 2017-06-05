#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 数据封装
# __init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身
# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
class Geek(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    
    def Print(self):
        print('%s: %s' % (self.__name, self.__score))

    def Abs(self):
        if self.__score > 0:
            print(self.__score)
        else:
            print(-(self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

data = Geek('zhangyi', 26)
data.Print()
data.Abs()
print(data.get_name())
print(data.get_score())
print(data._Geek__name)

# 继承 多态
# 当子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()，在代码运行的时候，总是会调用子类的run()。这样，我们就获得了继承的另一个好处：多态。
class Admin(object):
    
    def run(self):
        print('Admin 的打印...')

class Dog(Admin):
    
    def run(self):
        print('Dog 的打印...')

    def new(self):
        print('Dog 新功能...')

class Cat(Admin):
    
    def run(self):
        print('Cat 的打印...')


admin = Admin()
admin.run()

dog = Dog()
dog.run()
dog.new()

cat = Cat()
cat.run()

# 获取对象信息
# 判断对象类型，使用type()函数
# 判断一个变量是否是某个类型可以用isinstance()判断：
# 获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list
# 配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态
class MyObject(object):

    def __init__(self):
        self.x = 9
    def power(self):
        return  self.x * self.x

obj = MyObject()

print(hasattr(obj, 'x')) # 有属性'x'吗？
print(obj.x)
print(hasattr(obj, 'y')) # 有属性'y'吗？
print(setattr(obj, 'y', 19)) # 设置一个属性'y'
print(hasattr(obj, 'y')) # 有属性'y'吗？
print(getattr(obj, 'y')) # 获取属性'y'
print(obj.y) # 获取属性'y'

# 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性
# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

