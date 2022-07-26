"""
Завдання​а

У цьому домашньому завданні ми:

Додамо поле для дня народження Birthday. Це поле не обов'язкове, але може бути тільки одне.
Додамо функціонал роботи з Birthday у клас Record, а саме функцію days_to_birthday, яка повертає кількість днів до наступного дня народження.
Додамо функціонал перевірки на правильність наведених значень для полів Phone, Birthday.
Додамо пагінацію (посторінковий висновок) для AddressBook для ситуацій, коли книга дуже велика і треба показати вміст частинами, а не все одразу. 
Реалізуємо це через створення ітератора за записами.
Критерії прийому:​

AddressBook реалізує метод iterator, який повертає генератор за записами AddressBook і за одну ітерацію повертає уявлення для N записів.
Клас Record приймає ще один додатковий (опціональний) аргумент класу Birthday
Клас Record реалізує метод days_to_birthday, який повертає кількість днів до наступного дня народження контакту, якщо день народження заданий.
setter та getter логіку для атрибутів value спадкоємців Field.
Перевірку на коректність веденого номера телефону setter для value класу Phone.
Перевірку на коректність веденого дня народження setter для value класу Birthday.
"""

from collections import UserDict
from datetime import datetime, timedelta
from typing import List
import re

class Field:
    def __init__(self, value):
        self.value = value
        self._value = value
class Name(Field):
    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, value: str):
        if not isinstance(value, str):
            raise ValueError('Invalid name (string)')
        self._value = value
class Phone(Field):
    def __str__(self):
        return f'{self.value}'
    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, value: str):
        if 14 > len(value) > 9:
            self._value = value
        else:
            raise ValueError('Введіть номер у форматі +380XXXXXXXXX')
class Birthday(Field):
    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, date):
        if date:
            try:
                self._value = datetime.strptime(date, '%d-%m-%Y').date()
            except ValueError:
                print('Введіть дату у форматі день-місяць-рік (дд-мм-рррр)')
        self._value = date
class Record:
    def __init__(self, name: Name, phone: List[Phone] = [], birthday: Birthday = None):
        self.name = name
        self.phones = phone
        self.birthday = birthday
        # if phone:
        #     self.add_phone(phone)
    def add_phone(self, phone):
        self.phones.append(phone)
    def change_phone(self, phone: Phone, new_phone: Phone):
        if self.remove_record(phone):
            self.phones.append(new_phone)
            return new_phone
    def remove_record(self, phone: Phone):
        for i, phone in enumerate(self.phones):
            if phone.value == phone.value:
                return self.phones.pop(i)
    def __repr__(self):
        if self.birthday is None:
            return f'{self.name.value} : {str(*self.phones)}'
        else:
            return f'{self.name.value} : {str(*self.phones)}, Birthday: {self.birthday.value}'
    def day_birthday(self, birthday: Birthday):
        current_data = datetime.now()
        pattern = self.birthday.value.replace(year=current_data.year)
        diff = pattern - current_data.date()
        if diff.days > 0:
            return f'День народження через {diff.days} днів'
        else:
            diff1 = diff.days + 365
            return f'День народження через {diff1} днів'
class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record
    def iterator(self, maximum):
        count = 0
        for i in self.data:
            if count < maximum:
                count += 1
                yield self.data[i]
        else:
            raise StopIteration
def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "This key not found try again"
        except TypeError:
            return "Type not supported try again"
        except ValueError:
            return "Incorrect value try again"
        except AttributeError:
            return "Incorrect attribute try again"
        except StopIteration:
            return "That's oll"
        except RuntimeError:
            return "That's oll"
    return wrapper
def input_exit(*args):
    return 'До побачення, на все добре'
def input_hello(*args):
    return "Чим можу вам допомогти?"
def input_help(*args):
   return """ Ви можете скористатися наступними командами:
                add - Додати ім'я та номер телефону
                change - змінити контакт
                all - показати всі контакти"""
books = AddressBook()
@input_error
def input_add(*args):
    name = Name(args[0])
    phone = Phone(args[1])
    try:
        birthday = Birthday(args[2])
    except IndexError:
        birthday = None
    records = Record(name=name, phone=[phone], birthday=birthday)
    books.add_record(records)
    return f'Контакт успішно доданий'
@input_error
def input_change(*args):
    phone = Phone(args[1])
    new_phone = Phone(args[1])
    record = books.data[args[0]]
    result = record.change_phone(phone, new_phone)
    if result:
        return f'Контакт {record.name.value} успішно змінено'
@input_error
def input_phone(*args):
    return books.get(args[0])
def input_show(*args):
    return "\n".join([f"{v} " for v in books.values()])
def input_birthday(*args):
    rec = books[args[0]]
    result = (repr(rec))
    result1 = re.search(r"\d{2}-\d{2}-\d{4}", result)
    birt = Birthday(result1.group())
    rec_func = rec.day_birthday(birt)
    return rec_func
COMMANDS = {
    input_exit: ["good bye", 'Допобачення', '.', 'exit'],
    input_hello: ['hello', 'Привіт'],
    input_help: ['help', 'Допомога'],
    input_add: ['add', 'Додати'],
    input_change: ["change", 'змінити'],
    input_phone: ["phone"],
    input_show: ["all"],
    input_birthday: ['birthday']
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
if __name__ == '__main__':
    main()