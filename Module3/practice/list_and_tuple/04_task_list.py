# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех положительных элементов.

# TODO: your code here
numbers = (2, 4, -10, -12, -14, 8, 25)
summa = 0
for number in numbers:
    if number > 0:
        summa += number
print("сумма", summa)
