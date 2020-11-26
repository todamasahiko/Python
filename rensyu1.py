# coding: utf-8
initial == 'k'
point >= 80 and < 256
bmi < 20 or > 25
year % 4 == 0 # year / 4
not(day in [28, 30, 31]) # day != 28 and 30 and 31

print('これは自動挨拶プログラムです。')
isError = False
n = 99
if isError == False and n < 100:
	print('正解！')
number = int(input('数値を入力>>'))
if number % 2 == 0:
	print('偶数')
else:
	print('奇数')
say = input('挨拶をしてみましょう。>>')
if say == 'こんにちは':
	print('はい、こんにちは')
elif say == '調子はどうですか。':
	print('元気だよ。')
elif say == 'そろそろ帰るね':
	print('うん、またね。')
else:
	print('どうしたの。')


month = int(input('今は何月ですか。>>'))
if month in (1, 3, 5, 7, 8, 10, 12):
	print('月末は31日まで！') 
else:
	if month != 2:
		print('月末は30日まで！') #4, 6, 9, 11
	else:
		print('年間で最も寒い月！！！') #2
	print('年が明けてから')
print('{}ヶ月が経ったね。'.format(month))