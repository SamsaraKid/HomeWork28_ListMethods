from random import randint as rand

nums = []

for i in range(30):
    nums.append(rand(10, 50))

nums1 = set(nums)

print('Исходный массив:', nums)
print('Набор:', nums1)

for i in range(3):
    print('Максимум %d =' % (i + 1), max(nums1))
    nums1.remove(max(nums1))
