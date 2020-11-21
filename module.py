# coding: utf-8
text = input('何を記録しますか。>>')
file = open('diary.txt', 'a')
file.write(text + '\n')
file.close()

text = input('今日起こった出来事を教えてね。>>')
with open('diary.txt', 'a') as file:
	file.write(text + '\n')