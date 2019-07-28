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


class Cat(Animal):

    def catch(self):
        print("抓老鼠")

# 创建一个哮天犬对像

xtq = XiaoTianQuan()
xtq.eat()
xtq.bark()
xtq.fly()
xtq.run()
xtq.sleep()
# xtq.catch()
