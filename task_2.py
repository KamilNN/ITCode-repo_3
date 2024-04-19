print("------Задание 2------")
test_list = ["Hello", "Django", "Hola", "Thelongestword", "simple"]
max_length = 0
index = -1
for i in range(len(test_list)):
    if len(test_list[i]) > max_length:
        max_length = len(test_list[i])
        index = i
print("Самое длинное слово: ", test_list[index])

max_length = 0
index = -1
el = 0
while el < len(test_list):
    if len(test_list[el]) > max_length:
        max_length = len(test_list[el])
        index = el
    el += 1
print("Самое длинное слово: ", test_list[index])