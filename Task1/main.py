# Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def input_int_number(message):
    while(True):
        n = input(message)
        if n.isdigit():
            return int(n)
        else:
            print("Вы ввели не число.")

element = input_int_number("Введите первый элемент: ")
diff = input_int_number("Введите разницу: ")
steps = input_int_number("Введите количество элементов: ")

arithmetic_progression = []

for i in range(1, steps + 1):
    arithmetic_progression.append(element + (i - 1) * diff)

print(* arithmetic_progression)