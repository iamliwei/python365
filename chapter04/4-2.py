# 一个使用get()的简单数据库
# 在这里插入代码清单4-1中的数据库（字典people

userinfo={
    'alice':{
        'phone':'12412',
        'addr':'1212'
    },
    'test2': {
        'phone': '112412',
        'addr': '11212'
    }
}

# 电话号码和地址的描述性标签，供打印输出时使用

labels = {
    'phone': 'phone number',
    'addr': 'address'
}

name=input('name:')

# 要查找电话号码还是地址？
request = input('Phone number (p) or address (a)? ')
# 使用正确的键：
if request == 'p': key = 'phone'
if request == 'a': key = 'addr'

#使用get提供的默认值
person=userinfo.get(name,{})
label=labels.get(key,key)
result=person.get(key,'not available')

if name in userinfo:
    print("{}'s {} is {}.".format(name,label,result))
else:
    print('您要查找的信息不存在！！')