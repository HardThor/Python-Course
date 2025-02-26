"""Завдання 3: Відлік за допомогою циклу while
Програма, яка:

Запитує число від користувача.
Використовує цикл while, щоб вивести відлік від введеного числа до 0.
Використовує оператор break для виходу з циклу, коли число стане меншим за 0."""


        
number = input("Enter number: ")
number = float(number)
while True:
    print(number)
    number = number - 1
    if number < 0:
        break
# Або цикл в циклі який робить запит на повторне веденя числа
while True:
    number = input("Enter number: ")
    number = int(number)
    while True:
        print(number)
        number = number - 1
        if number < 0:
            break