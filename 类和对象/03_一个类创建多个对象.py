# 1.一个类可以创建多个对象；2.多个对象都调用函数的时候，self地址不相同
class Washer():
    def wash(self):  #这个函数即实例方法或对象方法
        print("能洗衣服")
        print(self)

haier1 = Washer()
haier1.wash()

haier2 = Washer()
haier2.wash()