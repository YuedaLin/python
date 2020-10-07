class Washer():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def wash(self): # 添加实例方法，访问实例属性
        print(f"洗衣机的宽度是{self.width}")
        print(f"洗衣机的高度是{self.height}")

haier1 = Washer(400, 500)
haier1.wash()

haier2 = Washer(1000, 1200)
haier2.wash()