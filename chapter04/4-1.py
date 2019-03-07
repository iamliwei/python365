# 一个简单的数据库
# 一个将人名用作键的字典。每个人都用一个字典表示，
#  字典包含键'phone'和'addr'，它们分别与电话号码和地址相关联

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

labels = {  'phone': 'phone number',    'addr': 'address' }

name=input('name:')

# 要查找电话号码还是地址？
request = input('Phone number (p) or address (a)? ')
# 使用正确的键：
if request == 'p': key = 'phone'
if request == 'a': key = 'addr'

if name in userinfo:
    print("{}'s {} is {}.".format(name, labels[key], userinfo[name][key]))
else:
    print('您要查找的信息不存在！！')