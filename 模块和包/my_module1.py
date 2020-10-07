# 完成任意两个数的加法运算
def testA(a, b):
    # print(a + b)
    return a + b

# 测试信息
# __name__是系统变量，是模块的标识符，值是：如果是自身模块值是__main__，否则是当前模块的名字
# 只在当前文件中调用函数，其他导入的文件内容不符合该条件，则不执行testA函数调用
if __name__ == '__main__':
    print(testA(1, 2))