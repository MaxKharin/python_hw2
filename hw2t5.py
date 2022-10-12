# Реализуйте алгоритм перемешивания списка.
# (Без использования библиотеки random)

lis = [1, 2, 3, 4, 5, 6]

for i in lis:
    while lis[i] == lis[-i]:
        lis.insert(0, lis[-1])
        lis.pop()
        lis.insert(3, lis[-1])
        i += 1
        lis.pop()
        print(lis)