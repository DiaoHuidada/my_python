# list_name = ["tom","car","phone","computer"]
# string = str(list_name.title())
# print(string)

#开头大写
s = "a s d  fsa fa f "
print(s.title())

#全部小写
ss = "SD SAD SD  D  FA  ASZ V"
print(ss.lower())

print(s.upper())

#去左边除空格
name = " tom "
print(name.lstrip())

#去除右边空格
print(name.rstrip())

#去除前后空格
print(name.strip())




################################################################
print("..................list列表.............................")

list_name = ['phone','car','computer','xiaoming']

#添加list
list_name.append('lisi')
print(list_name)

list_name.insert(0,'iphone')
print(list_name)

#查看长度
len(list_name)
print("list_name的长度是:  "+str(len(list_name)))

#删除list
del list_name[0]
print(list_name)

list_name.pop(1)
print(list_name)

list_name.remove("lisi")
print(list_name)

list_name[2]='小明'
print(list_name)

#排序
list_name.sort()
print(list_name)

#倒序
list_name.sort(reverse=True)
print(list_name)


################################################################
print("..................for循环.............................")
for i in range(1,21):
    print(i)

for index in list_name:
    print(index)



################################################################
print("..................while循环.............................")

while 20>10:
    print("hello world")
    break



