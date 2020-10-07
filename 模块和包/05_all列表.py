# 如果一个模块文件中有__all__变量，当使用 from xx import * 导入时，只能导入这个列表中的元素
from my_module2 import  *
print(testA(1, 2))

# print(testB(1, 2))