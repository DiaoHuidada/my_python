# name = ['diao dada','huidada','xidada']
# #print(name[2])
# new_name = name.pop()
# print(new_name)
#
# #在末尾添加
# name.append('zhangsan')
# print(name)
#
# #在索引处添加
# name.insert(0,'lisi')
# print(name)
#
# #根据索引删除元素
# del name[1]
# print(name)
#
# #删除末尾元素(需要赋值给新变量)
# new_name = name.pop()
# print(new_name)
#
# #根据元素内容删除元素
# name.remove('huidada')
# print("ss" + name)

#键值对
Phone={'iphone x':8888,'xiaomi 8':2999,'hw':3999}
print(Phone)
#根据键找值
my_phone = Phone['iphone x']
print(my_phone)
#根据键修改值
my_phone = Phone['iphone x']=5999
print(my_phone)