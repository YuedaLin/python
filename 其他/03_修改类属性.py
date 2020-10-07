# 类属性只能通过类对象修改
# 1.定义类，定义类属性
class Dog():
    tooth = 10

# 2.创建对象
wangcai = Dog()
xiaohei = Dog()

# 3.通过类修改属性
# Dog.tooth = 12
# print(Dog.tooth)
# print(xiaohei.tooth)

# 4.测试通过对象修改属性
xiaohei.tooth = 20
print(Dog.tooth)
print(xiaohei.tooth)
print((wangcai.tooth))
