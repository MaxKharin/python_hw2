# Задайте список из n чисел последовательности
# (1 + (1/n))^n и выведите на экран их сумму.
# Пример:
# Для n = 5: сумма = 11,55

n = int(input('Enter your number, please: '))
summ = 0
for i in range(1, n + 1):
    i = (1 + (1 / i)) ** i
    summ += i
    i += 1
print('The sum of the numbers is ', round(summ, 2))
