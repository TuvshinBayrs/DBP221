# 1
# n = int(input())
# for i in range(n + 1):
#     k = "*"*i
#     i += 1
#     print(k)
# 2
# n = int(input())
# for i in range(n + 1):
#     k = "*"*i
#     i +=1
#     print([k])
# # # 3
# students = {
# 'Bat': 18, 'Oyun': 22, 'Dulam': 21, 'Suren': 20
# }
# list = []
# for key, value in students.items():
#     if value == max(students.values()) or value == min(students.values()):
#         list.append(key)
#         list.reverse()     
# print(tuple(list))  
# 4  
import numpy as np
arr = np.arange(1, 1001)
sum = 0
for i in arr:
    if i % 3 == 0 or i % 7 == 0:
        sum += i 
print(sum)
