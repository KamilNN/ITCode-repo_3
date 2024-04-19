print("------Задание 9------")
test_list_9 = [43, 56, 43, 56, 543, 12, 12, 43, 87, 87]
length = len(test_list_9)
for i in range(length-1):
    j = i + 1
    while j < length:
        if test_list_9[i] == test_list_9[j]:
            test_list_9.pop(j)
            length -= 1
        j += 1

print(test_list_9)