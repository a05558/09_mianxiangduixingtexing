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

class XiaoTianQuan(Dog):
    def fly(self):
        print("我会飞")
        
    def bark(self):        
        print("叫的跟神一样...")

xtq = XiaoTianQuan()
xtq.bark()

