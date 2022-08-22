"""
Напишіть консольного бота помічника, який розпізнаватиме команди, що вводяться з клавіатури, і відповідати відповідно до введеної команди.

Бот помічник повинен стати для нас прототипом додатка-асистента. Додаток-асистент в першому наближенні повинен уміти працювати з книгою контактів 
і календарем. У цій домашній роботі зосередимося на інтерфейсі самого бота. Найбільш простий і зручний на початковому етапі розробки інтерфейс - це 
консольний додаток CLI (Command Line Interface). CLI досить просто реалізувати. Будь-який CLI складається з трьох основних елементів:

Парсер команд. Частина, яка відповідає за розбір введених користувачем рядків, виділення з рядка ключових слів та модифікаторів команд.
Функції обробники команд — набір функцій, які ще називають handler, вони відповідають за безпосереднє виконання команд.
Цикл запит-відповідь. Ця частина програми відповідає за отримання від користувача даних та повернення користувачеві відповіді від функції-handlerа.
На першому етапі наш бот-асистент повинен вміти зберігати ім'я та номер телефону, знаходити номер телефону за ім'ям, змінювати записаний номер телефону, 
виводити в консоль всі записи, які зберіг. Щоб реалізувати таку нескладну логіку, скористаємося словником. У словнику будемо зберігати ім'я користувача 
як ключ і номер телефону як значення.

Умови​

Бот повинен перебувати в безкінечному циклі, чекаючи команди користувача.
Бот завершує свою роботу, якщо зустрічає слова: .
Бот не чутливий до регістру введених команд.
Бот приймає команди:
"hello", відповідає у консоль "How can I help you?"
"add ...". За цією командою бот зберігає у пам'яті (у словнику наприклад) новий контакт. 
Замість ... користувач вводить ім'я та номер телефону, обов'язково через пробіл.
"change ..." За цією командою бот зберігає в пам'яті новий номер телефону існуючого контакту. 
Замість ... користувач вводить ім'я та номер телефону, обов'язково через пробіл.
"phone ...." За цією командою бот виводить у консоль номер телефону для зазначеного контакту. 
Замість ... користувач вводить ім'я контакту, чий номер треба показати.
"show all". За цією командою бот виводить всі збереженні контакти з номерами телефонів у консоль.
"good bye", "close", "exit" по будь-якій з цих команд бот завершує свою роботу після того, як виведе у консоль "Good bye!".
Всі помилки введення користувача повинні оброблятися за допомогою декоратора input_error. 
Цей декоратор відповідає за повернення користувачеві повідомлень виду "Enter user name", "Give me name and phone please" і т.п. 
Декоратор input_error повинен обробляти винятки, що виникають у функціях-handler (KeyError, ValueError, IndexError) та повертати відповідну відповідь користувачеві.
Логіка команд реалізована в окремих функціях і ці функції приймають на вхід один або декілька рядків та повертають рядок.
Вся логіка взаємодії з користувачем реалізована у функції main, всі print та input відбуваються тільки там.
"""


dict = {}

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except TypeError:
            return f'Будь ласка введіть ім`я та номер телефону'
        except IndexError:
            return f'Будь ласка введіть ім`я та номер телефону'
        except KeyError:
            return f'Неіснуючий контакт'

    return wrapper

def input_exit(*args):
    return 'Допобачення, хорошого дня'

def input_hello(*args):
    return "Чим я можу вам допомогти?"

def input_help(*args):
   return """ Ви можете скористатися наступними командами:
                add - Додати ім'я та номер телефону
                change - змінити контакт
                all - показати всі контакти"""

@input_error
def input_add(name: str, phone: str):
    dict[name] = phone
    return f'Контакт {name} успішно добавлено'
#
#
@input_error
def input_change(name: str, phone: str):
    for i in dict.keys():
        if i != name:
            print('такого контакту неіснує')
            raise KeyError
        else:
            dict[name] = phone
    return f'Контакт {name} успішно змінено'

@input_error
def input_phone(name: str):
    return dict[name]

def input_show(*args):
    list = ['{:^10}:{:>15}'.format(k,v) for k,v in dict.items()]
    return "\n".join(list)


COMMANDS = {
    input_exit:["good bye", 'Допобачення', '.', 'exit'],
    input_hello:['hello', 'Привіт'],
    input_help:['help', 'Допомога'],
    input_add:['add', 'Додати'],
    input_change:["change", 'змінити'],
    input_phone:["phone"],
    input_show:["all"]
}


def parse_command(user_input: str):
    for k,v in COMMANDS.items():
        for i in v:
            if user_input.lower().startswith(i.lower()):
                return k, user_input[len(i):].strip().split(' ')


def main():
    while True:
        user_input = input('>>>')
        result, data = parse_command(user_input)
        print(result(*data))
        if result is input_exit:
            break


if __name__ == "__main__":
    main()