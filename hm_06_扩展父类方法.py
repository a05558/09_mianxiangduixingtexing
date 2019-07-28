#! /usr/bin/python3
class Animal:
    
    def eat(self):
        print("吃")
    def bark(self):
        print("喝")

    def run(seft):
        print("跑")

    def sleep(self):
        print("睡")


class Dog(Animal):
    # 子类拥有父类的所有属性和方法
    def bark(self):
        print("汪汪叫")

class XiaoTianQuan(Dog):        # 3. 增加其他子类代码 
    def bark(self):        
        # 1. 针对子类特有的需求, 编写代码
        print("像神一样的叫唤...")
        # 2. 使用super(). 调用原来在父类中封装的方法
        # super().bark()
        # 注意: 如果使用子类调用方法, 会出现递归调用 - 死循环
        # 父类名.方法(self)
        Dog.bark(self)
        # 3. 增加其他子类代码
        print("$%^*%^#%$%")
    def fly(self):
        print("我会飞")


xtq = XiaoTianQuan()
xtq.bark()

