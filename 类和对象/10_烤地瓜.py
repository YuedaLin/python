# 1.定义类：初始化属性、被烤和添加调料的方法、显示对象信息的str
class SweetPotato():
    def __init__(self):
        # 被烤的时间
        self.cook_time = 0
        # 地瓜的状态
        self.cool_state = '生的'
        # 调料列表
        self.condiments = []

    # 烤地瓜的方法
    def cook(self, time):
        self.cook_time += time
        if 0 <= self.cook_time < 3:
            self.cool_state = '生的'
        elif 3 <= self.cook_time < 5:
            self.cool_state = '半生不熟的'
        elif 5 <= self.cook_time < 8:
            self.cool_state = '熟的'
        elif 8 <= self.cook_time:
            self.cool_state = '烤糊了'

    # 添加调料的方法
    def add_condiments(self, condiment):
        self.condiments.append(condiment)


    def __str__(self):
        return f"这个地瓜被烤过的时间时{self.cook_time}, 状态是{self.cool_state}，调料有{self.condiments}"

# 2.创建对象并调用对应的实例方法
digua1 = SweetPotato()
print(digua1)
digua1.cook(2)
digua1.add_condiments('辣椒粉')
print(digua1)
digua1.cook(2)
digua1.add_condiments('胡椒粉')
print(digua1)