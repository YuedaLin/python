# 多继承就是一个类同时继承了多个父类
# 注意：当一个类同时继承多个类时，默认使用第一个父类的同名属性和方法
# 1.师傅类
class Master():
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')
# 定义学习类
class School():
    def __init__(self):
        self.kongfu = '[学校的煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

# 2.徒弟类，继承师傅类和学校类
class Prentice(Master, School):
    pass

# 3.用徒弟类创建对象
daqiu = Prentice()
print(daqiu.kongfu)
daqiu.make_cake()