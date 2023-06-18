# 4


# 5
n = int(input('Введите желаемую границу: '))
e = int(input('Введите исключающий аргумент: '))
i = 0
number = 1
print("\n")
while i <= n :
    if i % 2 == 0 and i % e != 0:
        number += i
        print(i)
    elif i % e == 0:
        print(i, " - кратное ", e)
    i += 1
print("\nСумма чётных элементов исключая кратные ", e, "-", number)