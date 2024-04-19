print("------Задание 8------")
test_list_8 = [44, 76, 22, 1233, 444, 566, 343, 3355, 6556, 6556]
check = True
for i in range(len(test_list_8)-1):
    for j in range(i+1, len(test_list_8)):
        if test_list_8[i] == test_list_8[j]:
            check = False
    if not check:
        break
if check:
    print("В списке нет дубликатов")
else:
    print("В списке есть дубликаты")
