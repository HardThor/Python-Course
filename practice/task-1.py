"""Завдання 1: Привітання користувача
Програма, яка:

Запитує ім’я користувача за допомогою input().
Запитує вік користувача і перетворює введене значення у число (використовуючи int()).
Використовує тернарний оператор для створення повідомлення:
Якщо вік ≥ 18, повідомлення має бути:
"Hello, {name}! You are an adult."
Інакше:
"Hello, {name}! You are a minor."
Виводить повідомлення за допомогою print()."""

name = str(input("What is your name: "))
age = int(input("Your age: "))
user_age = age >= 18
st = f"Hello, {name}! You are an adult." if age else f"Hello, {name}! You are a minor."
print(st)