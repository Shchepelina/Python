#Задача 1: Найдите сумму цифр трехзначного числа.
#123 -> 6 (1 + 2 + 3)
#100 -> 1 (1 + 0 + 0)

num = int(input('Введите трехзначное число: '))
a = num % 10
b = num // 10 % 10
c = num // 100 % 10
print(a + b + c, '(', c, '+', b, '+', a, ')')