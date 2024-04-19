print("------Задание 4------")
test_list_4 = ['hello', 3, 3.5, 'python', 44, 32, 22.4, 2, 44, 3]
print("Каждый третий элемент числа")
for count, el in enumerate(test_list_4):
    if (count+1)%3 == 0 and count != 0:
        print(el)