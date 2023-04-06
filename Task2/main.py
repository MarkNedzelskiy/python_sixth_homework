# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 5
# 15
# Вывод: [1, 9, 13, 14, 19]

from random import randint

def input_int_number(message):
    while(True):
        n = input(message)
        if n.isdigit():
            return int(n)
        else:
            print("Вы ввели не число.")

list_len = input_int_number("Введите длину списка: ")
list_numbers = []

for i in range(list_len):
    list_numbers.append(randint(0, 20))

low_limit = input_int_number("Введите нижний порог для выборки: ")
high_limit = input_int_number("Введите верхний порог для выборки: ")

def search_numbers(low, high, array):
    temp_list = []
    for i in range(len(array)):
        if low < array[i] < high:
            temp_list.append(i)
    return temp_list

print(list_numbers)
print(search_numbers(low_limit, high_limit, list_numbers))
