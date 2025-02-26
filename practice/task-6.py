"""Завдання 6: Розширене використання винятків
Програма, яка:

Запитує від користувача число.
Використовує конструкцію try...except...else...finally:
try: спробуй перетворити введене значення в число.
except: якщо виникне помилка (наприклад, ValueError), виведи повідомлення "Invalid input, please enter a number."
else: якщо перетворення пройшло успішно, обчисли квадрат цього числа та виведи результат.
finally: виведи повідомлення "End of program." незалежно від того, чи була помилка чи ні."""

user_input = input("Enter number: ")
try:
    user_input = float(user_input)
except ValueError:
    print("Invalid input, please enter a number")
else:
    raising = (user_input ** 2)
    print(raising)
finally:
    print("End of program.")