# Задайте число N и создайте список, заполненный числами
# из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input('Enter your n number, please: '))
lis = []
if n > 0:
    for i in range(-n, n + 1):
        lis.append(i)
        i += 1
    print(lis)
else:
    print('Enter a number bigger than 0')

# data = open('file.txt', 'a')
# data.write('-1 \n')
# data.write('2 \n')
# data.close()

result = 1
path = 'file.txt'
data = open(path, 'r')
for line in data:
    result *= lis[int(line)]
data.close()
print('The multiplication product is', result)