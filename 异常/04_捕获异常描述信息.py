# 把要捕获的异常类型的名字，以元组的方式书写到except后面
try:
    print(num)
    # print(1/0)
except (ZeroDivisionError, NameError) as result:
    print(result)