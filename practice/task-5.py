"""Завдання 5: Виведення непарних чисел за допомогою циклу while та continue
Програма, яка:

За допомогою циклу while виводить непарні числа від 1 до 10.
Використовує оператор continue для пропуску чисел, які діляться на 2 без залишку."""

user_input = int(input("Enter number: "))

while user_input < 10:
    user_input = user_input + 1
    if not user_input % 2:
        continue
    print(user_input)