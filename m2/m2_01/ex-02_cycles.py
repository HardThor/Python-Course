"""Цикли"""
count = 0
while count <= 5:
    print(count)
    count += 1 # Аутоінкремент - це збільшення значення змінної на одиницю. Це дуже поширена операція в програмуванні, особливо в циклах! count -= 1 Зворотна операція - аутодекремент
    print(count)

"""Переривання циклу - break """
stuff = ""
while True:
    stuff = input("String to capitalize [type q to quit]:")
    if stuff == "q":
        break # використовується для повного переривання циклу ітерації
    print(stuff.capitalize()) #capitalize()використовується для того, щоб зробити першу літеру рядка великою, а всі інші — маленькими.Метод не змінює початковий рядок, а повертає новий. Перетворює лише першу літеру на велику, навіть якщо були інші великі літери в середині рядка метод зручний для форматування тексту, коли потрібно привести його до більш читабельного вигляду!
print("Bye Bye...")

"""Вічний цикл while - continue, break"""
name = ""
while True:
    name = input("Who are you?")
    if name != "Jack":
        continue
    print ("Hello Jack. What is the password?")
    while True: #Цикл в циклі
        password = input ("Plase set password:")
        if password == "1234":
                break
    print("OK")
    break
# """Цикл for"""
# fruit = "aplle"
# for char in fruit:
#     print(char)

# print("Test:")
# test = "aplle"
# for i in range(len(test)):
#     print(f"Iteration: {i}")

# print("************")
# print("Test_2:")
# for i in range(5):
#     print(f"iteration: {i}")
# # Тотожний варіант ітерацій циклу for як би він правцював у циклі while але частіше використовується цикл for
# # За допомогою якого відбувається ітерація по обєктам а не створювати ітерацію для ітерації через while
# # Цикл for виконує ітерацію по діапазону чисел за допомогою range().
# # Аналогічний результат можна отримати з циклом while, але for зручніше, 
# # Коли треба просто перебрати елементи послідовності або виконати фіксовану кількість ітерацій.
# print("------------")
# print("Test_3:")
# i = 0
# while i < 5:
#     print(f"iteration: {i}")
#     i = i + 1