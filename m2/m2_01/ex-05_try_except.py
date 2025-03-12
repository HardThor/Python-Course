"""Винятки"""
# val_1 = int(input("Please set first value: "))
# val_2 = int(input("Please set second value: "))
result = 0

try:
    val_1 = int(input("Please set first value: "))
    val_2 = int(input("Please set second value: "))
    result = val_1 / val_2
    print(result)
except ZeroDivisionError:
    print("Не можна ділити на нуль!")
# except ValueError as e:
#     print(f"Літера {e}")
finally:
    print("End of calc")

