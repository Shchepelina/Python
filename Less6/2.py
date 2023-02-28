#Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
#(т.е. не меньше заданного минимума и не больше заданного максимума)

import random
list=[random.randint(-50, 50) for i in range(random.randint(10,20))]
print(*list)

max =int(input("Введите максимальное число: "))
min =int(input("Введите миниимальное число: "))

listi=[]

if max>=min:
   for i in range(len(list)):
      if max>=list[i] and min<=list[i]:
          listi.append(i)

print("Кол-во чисел:",len(listi))
print("Индексы:",listi)