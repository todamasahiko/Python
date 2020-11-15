# coding: utf-8

members = ['John', 'Mike', 'Jack']
members.append('Charotte')
members.remove('Mike')
members[0] = 'Anubis'
print(members)
print(members[2])

scores = {'Japanese Language':70, 'Mathmatics':80, 'Science':90, 'Social Studies':100}
# total = sum(scores)
# avg = total / len(scores)
# print(scores[0:2])
# print(scores[1:])
# print(scores[:2])
# print(scores[:])
# print(scores[-3])
# print('合計は{}点、平均は{}点です。'.format(total,avg))

points = (1, 2, 3)
print(points)
print(points[2])

numbers = {10, 20, 30, 30}
numbers.add(40)
print(numbers)