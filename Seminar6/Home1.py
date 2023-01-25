# Дана последовательность чисел. 
# Получить список уникальных элементов заданной последовательности.
# Пример: 
#     [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10].

from random import *

nums = [randint(1, 15) for i in range(16)]
print('Исходный список: ', nums, '\n')

nums1 = [i for i in nums if nums.count(i) == 1]  
nums2 = list(filter(lambda x: nums.count(x) == 1, nums))   
 

print('Список уникальных элементов: ', nums1)
print('Список уникальных элементов: ', nums2, '\n')