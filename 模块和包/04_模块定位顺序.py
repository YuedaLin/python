"""
搜索顺序：
1.当前目录
2.如果不在当前目录下，Python搜索在shell变量下PYTHONPATH下的每个目录
3.如果都找不到，Python会察看默认路径。
注意：
1.自己的文件名不要和已有的模块名重复
2.使用 from 模块名 import 功能 的时候，如果功能名字重复，调用的是最后定义或者导入的功能
"""

# import random
# num = random.randint(1, 5)
# print(num)


# 定义函数 sleep
# def sleep():
#     print('这是自定义的sleep')
#
# from time import sleep

# sleep(2)

# 拓展：名字重复的严重性
# 问题：import 模块名  是否需要担心功能名字重复的问题 --不需要
import time
print(time)

time = 1   # 覆盖掉之前的模块
print(time)

# 问题：为什么变量也能覆盖模块？  --在Python语言中，数据是通过 引用 传递的