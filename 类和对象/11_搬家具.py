class Furniture():
    def __init__(self, name, area):
        self.name = name
        self.area = area

class Home():
    def __init__(self, address, area):
        # 房屋地理位置，面积，剩余面积，家具列表
        self.address = address
        self.area = area
        self.free_area = area
        self.furniture = []

    def __str__(self):
        return f'房子的地理位置在{self.address}, 面积是{self.area}, 剩余面积是{self.free_area}, 家具有{self.furniture}'

    def add_furniture(self, item):
        if self.free_area >= item.area:
            self.furniture.append(item.name)
            self.free_area -= item.area
        else:
            print(f'{item.name}太大，房子剩余面积不足，无法容纳')

bed = Furniture('双人床', 6)
sofa = Furniture('沙发', 3)
board = Furniture('篮球场', 1000)

home1 = Home('北京', 100)
print(home1)
home1.add_furniture(bed)
print(home1)
home1.add_furniture(board)
print(home1)