# coding: utf-8
count = 0
while count < 3:
	count += 1
	print('ひつじが{}匹'.format(count))
print('おやすみ')

is_awake = True
count = 0
while is_awake == True:
    count += 1
    print('ひつじが{}匹'.format(count))
    key = input('寝そうですか。（yes/no）')
    if key == 'yes':
    	is_awake = False
print('おやすみ')

count = 0
student_num = int(input('生徒数を入力'))
score_list = list()
while count < student_num:
	count += 1
	score = input('{}人目の点数を入力'.format(count))
	score_list.append(score)
print(score_list)
total = sum(score_list)
print('平均点は{}。'.format(total / student_num))

scores = [55, 77, 33, 99]
count = 0
while count < len(scores):
	if scores[count] >= 60:
		print('合格です。おめでとうございます。')
	else:
		print('不合格です。追試を受けてもらいます。'）
	count += 1

for num in range(3):
	print('ヨーソロー')

ages = [5, 7, 9, 12, 16, 18, 20, 24, 27, 30]
num = 5
samples = list()
    for data in ages:
        if 20 <= data >= 30:
            samples.append(data)
            if len(samples) == num:
                break
    print(samples)

ages = [5, 7, 9, 12, 16, 18, 20, 24, 27, 30]
samples = list()
for data in ages:
	if not isinstance(data, int):
		continue
	if 20 <= data >= 30:
		continue
    samples.append(data)
print(samples)