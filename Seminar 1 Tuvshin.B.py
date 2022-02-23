# #1
# lists = ['python','php','java']
# print(lists[0:3])
a=3
print(a)

#2
#num = [5,8,2,1,3,4,5,10,19,20]
#c = 0
#for i in num:
#    c = c + i
#    i = i + 1 
#print(c)

#3
#num = [5,4,2,7,5]
#def multiplier(x):
#    c = 1
#   for i in x:
#        c = c * i
#        i = i + 1
#    print(c)
#multiplier(num)

#4
# def multiply():
#    numbers = list(map(int, input('').split(',')))
#    multiplier = numbers[2]*numbers[-1]
#    print(multiplier)    
# multiply()

#5
#def func():
#    numbers = list(map(int, input('').split(',')))
#    x = max(numbers)
#    y = min(numbers)
#    print(x,y)

#6
#list = ['222','383','zkz']
#def samedigits(list):
#  k = 0
#  for i in list:
#    if  i[0] == i[-1]:
#      k += 1
#  return k
#print(samedigits(list))


#7
#numbers = list(map(int, input('').split(',')))
#list2 = set(numbers)
#print(list(list2))

#8
# list = []
# def func(list):
#     if len(list) == 0:
#         print('List is empty')  
#     else:
#         print('List is not empty')
# func(list)

#9
# alist = [11,23,4,5,6,7,8,2,3,8]
# del alist[3], alist[4], alist[5]
# print(alist)

#10,11
# numbers = (1,2,3,5,6,7,8,9,10,11)
# y = list(numbers)
# y.append(input())
# numbers = tuple(y)
# print(numbers)

#12
# numbers = (1,2,3,5,6,7,8,9,10,11)
# print(numbers[1],numbers[-2])

# 13
# y = input()
# cities = ('Tokyo','Seoul','UB','Manila',y)
# if y in cities:
#     print('Yes')


#14
# numbers = (1,2,3,5,6,7,8,9,10,11)
# k = 0
# for i in numbers:
#     print(i)
#     i += 1

#15 
# laugh = {'kk','jaja','haha'}
# laugh2 = {'hehe','hah'}
# nlaugh = laugh.union(laugh2)
# print(nlaugh)

#16
# laugh = {'kk','jaja','haha'}
# laugh2 = {'hehe','haha'}
# nlaugh = laugh.intersection(laugh2)
# print(nlaugh)

#17
# laugh = {'kk','jaja','haha'}
# length = len(laugh)

#18
# x = input()
# laugh = {'kk','jaja',x,'haha'}
# print(laugh)
# laugh.remove(x)
# print(laugh)

#19
# laugh = {'kk','jaja','haha'}
# laugh.clear()


#20
#laugh = {'kk','jaja','haha'}
#del laugh

#21
# from audioop import reverse
# import operator
# num = {2011: 198,2014: 100, 2015: 250}
# print(sorted(num.items(),key=operator.itemgetter(1)))


#22
# num = {'2011': '198','2014': '210', '2015': '250'}
# if '2011' in num:
#     print('Yes')
# else:
#     print('No')

#23
# num = {'2011': '198','2014': '210', '2015': '250'}
# if '198' in num.values():
#     print('Yes')
# else:
#     print('No')

#24
# num = {'2011': '198','2014': '210', '2015': '250'}
# for i,k in num.items():
#     print(i,k)

#25
# num = {'2011': '198','2014': '210', '2015': '250'}
# names = {'key1':'Venezuela','key2':'Mongolia'}
# num.update(names)
# for i,k in num.items():
#      print(i,k)

#26
# num = {'2011': 198,'2014': 210, '2015': 250}
# print(sum(num.values()))
