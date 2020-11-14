# coding: utf-8

import keyword
print(keyword.kwlist)

print(7)
print(25)
print(1 + 1)
print(2 * 2)
print(3 / 3)
print(6 % 3)
print('1' + '1')
print('もし' * 2)
print('おはよう諸君')
print('おはよう\n諸君\\')
print('\"と\'')

print(1 + 1 * 7)
print((1 + 1) * 7)

name, age = 'John', 33
print(name)
print(age)

print('半径7の円直径は')
ans = 7 * 2
print(ans)
print('円周は')
print(ans * 3.14)

old = 20
print('今年は')
print(old)
old = old + 1
print('来年は')
print(old)

#nickname = input('名前を教えて')
#print('ようこそ！' + nickname)

a = 1
print(type(a))

x = 3.14
y = int(x)
print(y)
print(type(y))
z = str(x)
print(z)
print(type(z))
print(z * 2)

name1 = '神様'
age1 = 77
print('我が名は{}、年は{}である').format(name1,age1)

name2 = '神'
age2 = 7
print(f'我が名は{name2}、年は{age2}である')