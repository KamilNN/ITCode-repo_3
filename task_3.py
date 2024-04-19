print("------Задание 3------")
fact = 1
number_3 = int(input("Введите число: "))
for i in range(2, number_3 + 1):
    print (fact, '*', i, '=', fact*i)
    fact *= i
print("Итоговый результат: ", fact)