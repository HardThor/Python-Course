"""Завдання 2: Обчислення суми двох чисел з обробкою винятків
Програма, яка:

Запитує два числа від користувача.
Перетворює введені значення у числа (використовуючи int() або float()).
Якщо користувач вводить нечислове значення, використай конструкцію try...except 
для обробки помилки (наприклад, ValueError) та виведи повідомлення про помилку.
Обчисли суму чисел і виведи її."""

first_number = input("Enter first number: ")
second_number = input("Enter second number: ")

try:
    first_number = float(first_number)
    second_number = float(second_number)
except ValueError:
    print(f"{first_number} is not a number")
    print(f"{second_number} is not a number")
else:
    calculation = (first_number + second_number)
    print(calculation)
finally:
    print("End of calculation")