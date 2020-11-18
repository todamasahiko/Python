# coding: utf-8
def hello(name):
	print('おはよう！{}ちゃん'.format(name))
hello('よしこ')
hello('ヨハネ')

def profile(name, age, hobby):
	print('彼女は{}。'.format(name))
	print('{}歳。'.format(age))
	print('{}を弾くのが好き。'.format(hobby))
profile('まき', 16, 'ピアノ')

def plus(x, y):
	answer = x * y
	return answer
answer = plus(2, 7)
print('掛けると{}'.format(answer))

def plus_and_minus(a, b):
    return a + b, a - b
next, prev = plus_and_minus(3, 8)

def eat(breakfast, lunch, dinner='納豆'):
	print('朝は{}を食べました。'.format(breakfast))
	print('昼は{}を食べました。'.format(lunch))
	print('夜は{}を食べました。'.format(dinner))
eat('ヨーグルト', 'そば')

name = 'まき'
def change_name():
    global name
    name = 'えり'
def hello():
    print(name + 'ちゃん、おはよう')
change_name()
hello()