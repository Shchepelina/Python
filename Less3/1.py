#Задача 1.
#Требуется вычислить, сколько раз встречается некоторое число X 
#в массиве A[1..N].
#Пользователь в первой строке вводит натуральное число N – 
#количество элементов в массиве. 
#В последующих строках записаны N целых чисел Ai.
#Последняя строка содержит число X.
#Пример
#5
#1 2 3 4 5
#3
#-> 1
n = input("Введите количество элементов: ")
m = input("Введите элементы: ")
x = input("Введите искомый элемент: ")
sum = 0
for i in range(len(m)): 
    if m[i] == x:
        sum += 1
print(sum)    