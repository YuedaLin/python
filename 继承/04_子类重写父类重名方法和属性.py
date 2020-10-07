# 结论：如果子类和父类拥有同名属性和方法，子类创建对象调用属性和方法时，调用的是子类的同名属性和方法
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
    def __init__(self):
        self.kongfu = '[独创的煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

# 3.用徒弟类创建对象
daqiu = Prentice()
print(daqiu.kongfu)
daqiu.make_cake()