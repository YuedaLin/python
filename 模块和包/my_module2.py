# 如果一个模块文件中有__all__变量，当使用 from xx import * 导入时，只能导入这个列表中的元素
__all__ = ['testA']

def testA(a, b):
    # print(a + b)
    return a + b

def testB(a, b):
    # print(a - b)
    return a - b