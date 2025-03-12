"""1. умови та умовні оператори"""
a = (7 < 9) and (7 < 11)
print(a) # True

b = 2 + 2  == 4 and not 2 + 2 == 5 and 2 * 2 == 2 + 2 # Спочатку виконуються усі арефметичні операції потім порівняння далі оперції заперечення далі оператор and далі or якщо він є.
print(b) # True 

name = "Tomas"
if name == "Tomas":
    print(f"Hello, {name}!")

c = "c"
print(ord(c))

ord("c")
99
ord("C")
67
a = "c"
b = "C"
c = a > b
print(c)
#True
c_1 = a < b
print(c_1)
#False

a_1 = True
b_1 = None
a = "statement_1" if b_1 else "statement_2"
print(a)

a, b = 6, 5 #Теж буде працювати але не рекомендовано. Далі в коді буде важкочитабельне.
max = f"{a} Більше" if a > b else f" {b} більше першого числа"
print(max)