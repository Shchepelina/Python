#На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. \
#Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
#Выведите минимальное количество монет, которые нужно перевернуть.
#Пример:
#5 -> 1 0 1 1 0

num = int(input("Введите число монеток "))
count = 0
for i in range(num):
    v = int(input("Какой стороной лежит монетка? 1- орел, 0 - решка "))
    if v == 1:
        count += 1
print("Минимальное количество монет, которые нужно перевернуть навно:", count if count<num/2 else num-count)
