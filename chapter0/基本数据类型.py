# type()不会认为子类是一种父类类型。
# isinstance()会认为子类是一种父类类型。

a,b,c,d = 20,5.5,True,4+3j
print(type(1),type(b),type(c),type(d))
print("-----------------------------")
print(isinstance(a,int))

# 您也可以使用del语句删除一些对象引用。