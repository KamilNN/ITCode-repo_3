print("------Задание 6------")
number = int(input("Введите число: "))
number = abs(number)
count = 0
while number > 0:
    count += 1
    number //= 10
print("Количество цифр:", count)

count = 0
number = int(input("Введите второе число: "))
number = str(abs(number))

for el in number:
    count += 1
print("Количество цифр:", count)
