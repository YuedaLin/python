# 1.师傅类
class Master():
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

# 2.徒弟类
class Prentice(Master):
    pass

# 3.用徒弟类创建对象
daqiu = Prentice()
print(daqiu.kongfu)
daqiu.make_cake()