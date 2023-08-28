import os

# 4


# 5
n = int(input('1.5. Введите желаемую границу: '))
e = int(input('Введите исключающий аргумент: '))
i = 1
number = 0
while i <= n :
    if i % 2 == 0 and i % e != 0:
        number += i
        print(i)
    elif i % e == 0:
        print(i, " - кратное ", e)
    i += 1
print("\nСумма чётных элементов исключая кратные ", e, "-", number)

# 6
year = int(input("\n1.6. Введите желаемый год: "))
leapnewy = 400; leapnewno = 100; leapold = 4
if year % leapold == 0:
    answ = "високосный."
elif year % leapnewy == 0 and year % leapnewno == 0:
    answ = "високосный по григорианскому календарю."
elif year % leapnewno == 0:
    answ = "невисокосный по григорианскому календарю."
else:
    answ = "невисокосный."
print("Данный год -", answ)

# 7
game = True
while game:
    number = int(input("\n1.7. Пожалуйста, введите число от 1 до 999:\n"))
    i = 0
    bot = number
    while 1 <= bot:
        bot /= 10
        i += 1
    if i == 1:
        wint = "Квадрат цифры -"
        number **= 2
        game = False
    elif i == 2:
        wint = "Разность цифер числа -"
        numa = number // 10
        numb = number % 10
        number = numa - numb
        game = False
    elif i == 3:
        wint = "Число наоборот -"
        j = 1
        bot = number
        str(number)
        number = ""
        while j <= bot:
            frag = bot % 10
            bot //= 10
            if frag != 0:
                rev = str(frag)
                number += rev
        game = False
print(wint, number)


# 8
tree = ""
levels = int(input("\n1.8. Введите желаемую высоту для ёлки: "))
wig, hei = levels + 5, levels
Pineview = [[0 for x in range(wig)] for y in range(hei)]
# for x in range(0, wig):
#     for y in range(0, hei):
#         Pineview[y][x] = "0"
for i in range(0, levels + 1):
    if i == 0:
        tree += "*"
        Pineview[levels - 1][i] = tree
    else:
        tree += "**"
        Pineview[levels - 1][i] = tree
for y in Pineview:
    for x in y:
        print(x, end=" ")
    print()
    # print(tree.center(os.get_terminal_size().columns))

# 9
limit = input("\n1.9. Нажмите любую кнопку чтобы вывести таблицу умножения.\n")
for x in range(2, 10):
    print("\n")
    for y in range (2, 11):
        print(x, "*", y, "=", x*y)
