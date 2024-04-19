print("------Задание 7------")
line_7 = input("Введите строку: ")
check = True
new_line_7 = ''.join(line_7.split())
new_line_7 = new_line_7.lower()

for i in range(len(new_line_7)):
    if new_line_7[i] != new_line_7[-(i+1)]:
        check = False
if check:
    print("Палиндром")
else:
    print("Не палиндром")
