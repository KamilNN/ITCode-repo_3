print("------Задание 1------")
n = 10345
sum = 0
for num in range(1, n+1):
    if num % 2 == 0:
        sum += num
print("Сумма четных чисел: ", sum)

sum = 0
num = 1
while num <= n:
    if num % 2 == 0:
        sum += num
    num += 1
print("Сумма четных чисел: ", sum)
