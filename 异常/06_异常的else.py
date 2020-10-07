# else表示的是如果没有异常要执行的代码
try:
    print(1)
    # print(1/0)
except Exception as result:
    print(result)
else:
    print(2)