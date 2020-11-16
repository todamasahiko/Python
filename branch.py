# coding: utf-8
name = 'よしこ'; print('私の名前は{}ではありません。'.format(name))

name = input('名前を教えて>>')
print('{}さん、よろしくね。'.format(name))
food = input('{}さんの好きな食べ物は？>>'.format(name))
if food == '寿司':
    print('THE日本食ですよね！')
else:
    print('{}もいいですね。'.format(food))

score = int(input('点数を入力してください'))
if score < 0 or score > 100:
	print('入力が間違っています。正確に入力し直してください')
elif score >= 70:
	print('合格です。おめでとうございます。')
else:
	print('不合格です。追試を受けてもらいます。')

print('質問にyesもしくはnoで回答してください。')
money = input('所持金はありますか。')
if money == 'yes':
	tight_eat = input('がっつり食べたいですか。')
	light_eat = input('軽く食べたいですか。')
	if tight_eat == 'yes':
		print('ラーメンはいかがですか。')
	elif light_eat == 'yes':
		print('サンドイッチはいかがですか。')
else:
	print('家で食べましょう。')