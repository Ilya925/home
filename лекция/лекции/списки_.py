"""списки (list)
тип данныйх - списки, стуктура данных - массив."""
from copy import deepcopy

#print(__doc__)
"""список - упорядоченный набор объектов"""
"""   8    1    2    3    4   """
nums = [22, 33, 44, 55, 99]
# """  -5   -4   -3   -2   -1   """
# print(nums[-3])
# print(nums[2])
# print(nums[-3:0:-1])
# print(nums[2::-1])
# print(nums[2:])
# print(nums[::-1]) # реверсивный вывод информации
#nums = [20, 30, [40, 50]]
#s = nums
#s = nums.copy()
#s = nums[:]
# s = deepcopy(nums)
# nums[0] = 200
# nums[-1][0] = 400
# print(nums)
# print(id(nums))
# print(id(s))
# print(s)
# nums[0:3] = 10, 20, 30
# print(nums)

ls = [10, 'Dasha', 5.45, True, [67,'Andre']]
lst = [['Masha', 18], ['Dasha', 22]]
name = ['Masha', 'Dasha']
age = [18, 22]
print(name[1], age[0])

nums = [22, 33, 44, 55, 99]
print(id(nums))
nums.append(100)  #временная сложгость0(1) - константная
nums.insert(3, 200)
#nums.extend([1, 2])
#nums +=[1, 2]
#nums = nums + [1, 2]

nums.pop() # удаляем последний элемент списка
n = nums.pop()
print(n)

print(id(nums))
print('n==', n)
print(nums)
print(len(nums))


nums = []
n = float(input('> '))
while n !== 273:
    nums.append(n)
    n = float(input('> '))
print()

