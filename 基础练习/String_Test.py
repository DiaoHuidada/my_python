string_str = " I am very Handsome. "

#lower()    所有转换成小写
print(string_str.lower())

#upper()   所有转换成大写
print(string_str.upper())

#lstrip()   去除左边空格
print(string_str.lstrip())

#rstrip()   去除右边空格
print(string_str.rstrip())

#strip()  去除左右两边空格
print(string_str.strip())

#len()   输出字符串长度
print("字符串长度： "+str(len(string_str)))

#count()   查找指定字符串出现的次数
string_str_count = string_str.count("b",0)
print("字符串出现的次数： "+str(string_str_count))

#find()   查找字符串中是否有指定字符串  没有返回-1
string_str_find = string_str.find('m',0)
print(string_str_find)

#index()   查找字符串中有没有指定的字符串  没有直接报错  有显示第一次出现的索引
string_str_index = string_str.index('a',0)
print(string_str_index)

#startswith()  检查是否以指定字符串开头  返回布尔值
string_str_startswith = string_str.startswith(' ',0)
print("是否以sub开头： "+str(string_str_startswith))

#endswith  检查是否以指定字符结尾   返回布尔值
string_str_endswith = string_str.endswith(' ',0)
print("是否以sub结尾： "+str(string_str_endswith))

#islower()  检查字符串是否都是小写  返回布尔值
string_str_islower = string_str.islower()
print("全部都是小写？？" + str(string_str_islower))

#isupper()   检查字符串是否都是大写  返回布尔值
string_str_isupper = string_str.isupper()
print("全部都是大写？？" + str(string_str_isupper))

#isalpha()  检查字符串是否都是字母组成
string_str_isalpha = string_str.isalpha()
print("是否都是字母？？ " + str(string_str_isalpha))

#isdigit()  检查字符串是否都是数字组成
string_str_isdigit = string_str.isdigit()
print("是否都是数字？？" + str(string_str_isdigit))

#replace()   替换字符串
string_str_replace = string_str.replace("I","i")
print(string_str_replace)




