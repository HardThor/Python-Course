"""Завдання: Обчислення факторіалу числа

Програму, яка:

Запитує у користувача введення числа.
Перетворює введене значення у ціле число. 
Якщо введене значення некоректне 
(не число або число менше 0), програма повинна обробити виняток і вивести відповідне повідомлення.
Обчислює факторіал цього числа за допомогою циклу (while або for).
Виводить результат.
Підказки:

Факторіал числа n (позначається n!) визначається як:
n! = n × (n-1) × (n-2) × ... × 1, для n > 0.
0! = 1.
Використовуй конструкцію try...except для обробки помилок при перетворенні введеного значення в 
int.
Переконайся, що якщо користувач вводить від’ємне число, програма повідомляє про помилку або 
просить ввести число заново."""

try:
    user_input = int(input("Please enter a number: "))
    if user_input < 0:
        raise ValueError("Negative input")
except ValueError:
    print("You entered a negative number or an invalid value. Please enter a positive number.")
else:
    factorial = 1
    for i in range(1, user_input + 1):
        factorial *= i
    print(f"The factorial of {user_input} is {factorial}.")
finally:
    print("The program has finished its work.")