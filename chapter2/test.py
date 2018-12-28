import feibo

feibo.fib(1000)
print("-----------------------")
result = feibo.fib2(100)
print(result)
_name = feibo.__name__
print(_name)

_name_ = feibo.__name__
if _name_ == '_main_':
    print('程序运行在自身')
else:
    print('程序在另一模块')