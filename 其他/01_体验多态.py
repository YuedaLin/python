# 定义：多态是一种使用对象的方法，子类重用父类方法，调用不同子类对象的相同方法，可以产生不同的执行结果

# 步骤：
# 1.定义父类，并提供公共方法；警犬 和 人
# 定义警犬这个类
class Dog():
    def work(self):
        print('指哪打哪。。。')

# 定义人这个类
class Person():
    def work_with_dog(self, dog):
        dog.work()

# 2.定义子类，并重写父类方法；定义2个类表示不同的警犬
class ArmyDog(Dog):
    def work(self):
        print('追击敌人。。。')

class DrugDog(Dog):
    def work(self):
        print('追查毒品。。。')

# 3.传递子类对象给调用者,传入不同的对象，观察执行的结果
ad = ArmyDog()
dd = DrugDog()

daqiu = Person()
daqiu.work_with_dog(ad)
daqiu.work_with_dog(dd)


