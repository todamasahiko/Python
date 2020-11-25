# coding: utf-8
1-1
⑴　2 + 10 * 5
➡︎ 2 + 50
➡︎ 52

⑵ '7' * (3 + 4)
➡︎  '7' * 7
➡︎ '7777777'

⑶ 'version {}'.format(3 + 2 * 0.1 + 9 * 0.01)
➡︎ 'version {}'.format(3 + 0.2 + 0.09)
➡︎ 'version {}'.format(3.29)
➡︎ 'version 3.29'

⑷ 4 * 'num' + '回目のTypeError'
➡︎ 'numnumnumnum' + '回目のTypeError'
➡︎ 'numnumnumnum 回目のTypeError'

1-2
⑴　var = 35 + num
  　var = 35 + 2
  　var = 37
  　varはint型

⑵　num += '5'
    2 += '5'
    エラー

⑶ GLOBAL = '世界' + str(num) + '箇国'
   GLOBAL = '世界' + str(2) + '箇国'
   GLOBAL = '世界' + '2' + '箇国'
   GLOBAL = '世界2箇国'
   GLOBALはstr型

⑷ check_code = num * (9 / 3)
   check_code = 2 * (3.0)
   check_code = 6.0
   check_codeはfloat型

1-3
print('これはBMI自動算出プログラムです。')
height = int(input('あなたの身長を入力してください>>')) / 100
weight = int(input('あなたの体重を入力してください>>'))
print('入力ありがとうございます。しばらくお待ちください')
bmi = weight / height / height
print('お待たせしました、あなたのBMIは {}です。'.format(bmi))

2-1
⑴47都道府県の都道府県名と人口➡︎ディクショナリ
⑵過去28日間分の1日あたりのWebサイトアクセス数➡リスト
⑶方角➡︎セット
⑷プログラミング言語の名称➡︎セット
⑸航空機200座席の予約状況（0=空席、1=予約済）➡︎ディクショナリ

2-2
print('これは試験結果自動計算プログラムです')
scores = []
scores.append(int(input('あなたの国語の点数を入力してください>>')))
scores.append(int(input('あなたの算数の点数を入力してください>>')))
scores.append(int(input('あなたの理科の点数を入力してください>>')))
scores.append(int(input('あなたの社会の点数を入力してください>>')))
scores.append(int(input('あなたの英語の点数を入力してください>>')))
print(f'あなたの5教科の試験結果の合計は{sum(scores)}点、平均は{sum(scores) / len(scores)}点です。')

2-3
print('これは相性診断自動プログラムです')
a = {'アニメ', '料理', 'ファッション', '抹茶', 'ダーツ'}
b = {'漫画', '食べ歩き', 'ファッション', 'チョコミント', 'カラオケ'}
input('準備ができたらEnterを押してね。')
common = a & b
total = a | b
compatibility_rate = len(common) / len(total) : 100
print(f'あなたたちの相性は{compatibility_rate}%です。')