a = int(input("Enter a number: "))

if a % 2 == 0 and a % 3 == 0:
    print("a кратно 2 і 3")

if not a % 2 and not a % 5:
    print("a кратно 2 і 5")

if a <= 10 or a >= 50:
    print("a не належить проміжутку (10, 50)")  # [10, 50)

if a > 10 and a < 50:
    print("a належить проміжутку (10, 50)")