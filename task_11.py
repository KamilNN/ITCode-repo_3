print("------Задание 11------")
print("Пн Вт Ср Чт Пт Сб Вс")
for i in range(1, 32):
    if i < 10:
        print(i, ' ', end='')
        if not i % 7:
            print()

    if i >= 10:
        print(i, '', end='')
        if not i % 7:
            print()
