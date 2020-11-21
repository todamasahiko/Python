# coding: utf-8
# userinfo = input('名前と血液型を入力>>')
# [name, blood] = userinfo.split(',')
# blood = blood.upper().strip()
# print('{}さんは{}型です。'.format(name,blood))

int_value1 = 0
int_value2 = int()
int_value3 = int(7)
list_value1 = []
list_value1 = list()
list_value1 = list(('りん', 'はなよ'))

scores1 = [78, 85, 100]
scores2 = [78, 85, 100]
print('scores1のidentity: {}'.format(id(scores1)))
print('scores2のidentity: {}'.format(id(scores2)))

if scores1 == scores2:
	print('scores1とscores2は同じ内容です。')
else:
	print('scores1とscores2は異なる内容です。')

if id(scores1) == id(scores2):
	print('scores1とscores2は同じ存在です。')
else:
	print('scores1とscores2は異なる存在です。')

scores1 = [78, 85, 100]
scores2 = [78, 85, 100]
print('scores1の先頭要素は{}'.format(scores1[0]))
print('scores2の先頭要素は{}'.format(scores2[0]))

print('変数scores2を変数scores1に代入する。')
scores1 = scores2

print('scores1の先頭要素を60に書き換える。')
scores1[0] = 60

print('60を代入したscores1の先頭要素は{}'.format(scores1[0]))
print('60を代入していないscores2の先頭要素は{}'.format(scores2[0]))

def add_suffix(names):
	for i in range(len(names)):
		names[i] = names[i] + 'ちゃん'
	return names

before_names = ['ちか', 'よう', 'りこ']
copied_names = list()
for n in before_names:
	copied_names.append(n)
after_names = add_suffix(copied_names)
print('ちゃん付後:' + after_names[0])
print('ちゃん付前:' + before_names[0])

def add_suffix(names):
	for i in range(len(names)):
		names[i] = names[i] + 'ちゃん'
	return names

before_names = ['だいや', 'まり', 'かなん']
copied_names = before_names.copy()
for n in before_names:
	copied_names.append(n)
after_names = add_suffix(copied_names)
print('ちゃん付後:' + after_names[0])
print('ちゃん付前:' + before_names[0])

def add_suffix(names):
	for i in range(len(names)):
		names[i] = names[i] + 'ちゃん'
	return names

before_names = ['よしこ', 'はなまる', 'るびぃ']
copied_names = before_names[:]
for n in before_names:
	copied_names.append(n)
after_names = add_suffix(copied_names)
print('ちゃん付後:' + after_names[0])
print('ちゃん付前:' + before_names[0])

def add_suffix(names):
	for i in range(len(names)):
		names[i] = names[i] + 'ちゃん'
	return names

before_names = ['まき', 'りん', 'はなよ']
import copy
copied_names = copy.copy(before_names)
for n in before_names:
	copied_names.append(n)
after_names = add_suffix(copied_names)
print('ちゃん付後:' + after_names[0])
print('ちゃん付前:' + before_names[0])

chara_name = list()
print('変更前のlistのidentity値: {}'.format(id(chara_name))
chara_name.append('ほのか')
print('変更後のlistのidentity値: {}'.format(id(chara_name))

name = `ことり`
print('変更前のstrのidentity値: {}'.format(id(name))
name = 'ちゅんちゅん' + name
print('変更後のstrのidentity値: {}'.format(id(name))