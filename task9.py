# Сколько встречается различных чисел в списке
# 1, 8, 3, 1, 2, 3

list_1 = [1, 8 ,3, 1, 2, 3] 
n = len(list_1)
print("Количество элементов в списке: ", n)

# x = len(set(list_1))
# print("количество уникадьных элементов: ", x)

for i in range(n):
    for j in range(n-i-1):
        if list_1[j] > list_1[n-1-i]:
            list_1[j], list_1[n-1-i] = list_1[n-1-i], list_1[j]
print(list_1)

count = 1 
for i in range(n-1):
    if list_1[i] != list_1[i+1]:
        count += 1
print(count)