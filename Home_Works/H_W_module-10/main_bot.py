"""
Завдання​

У цій домашній роботі ми продовжимо розвивати нашого віртуального асистента з CLI інтерфейсом.

Наш асистент вже вміє взаємодіяти з користувачем за допомогою командного рядка, отримуючи команди та аргументи та виконуючи потрібні дії. 

У цьому завданні треба буде попрацювати над внутрішньою логікою асистента, над тим, як зберігаються дані, які саме дані і що з ними можна зробити.

Застосуємо для цих цілей об'єктно-орієнтоване програмування. Спершу виділимо декілька сутностей (моделей) з якими працюватимемо.

У користувача буде адресна книга або книга контактів. Ця книга контактів містить записи. Кожен запис містить деякий набір полів.

Таким чином ми описали сутності (класи), які необхідно реалізувати. Далі розглянемо вимоги до цих класів та встановимо їх взаємозв'язок, правила, за якими вони будуть взаємодіяти.

Користувач взаємодіє з книгой контактів, додаючи, видаляючи та редагуючи записи. Також користувач повинен мати можливість шукати в книзі контактів записи за одному або декількома критеріями (полям).

Про поля також можна сказати, що вони можуть бути обов'язковими (ім'я) та необов'язковими (телефон або email наприклад). Також записи можуть містити декілька полів одного типу (декілька телефонів наприклад). 

Користувач повинен мати можливість додавати/видаляти/редагувати поля у будь-якому записі.

В цій домашній роботі ви повинні реалізувати такі класи:

Клас AddressBook, який успадковується від UserDict, та ми потім додамо логіку пошуку за записами до цього класу.
Клас Record, який відповідає за логіку додавання/видалення/редагування необов'язкових полів та зберігання обов'язкового поля Name.
Клас Field, який буде батьківським для всіх полів, у ньому потім реалізуємо логіку загальну для всіх полів.
Клас Name, обов'язкове поле з ім'ям.
Клас Phone, необов'язкове поле з телефоном та таких один запис (Record) може містити кілька.
Критерії прийому

Реалізовано всі класи із завдання.
Записи Record у AddressBook зберігаються як значення у словнику. В якості ключів використовується значення Record.name.value.
Record зберігає об'єкт Name в окремому атрибуті.
Record зберігає список об'єктів Phone в окремому атрибуті.
Record реалізує методи для додавання/видалення/редагування об'єктів Phone.
AddressBook реалізує метод add_record, який додає Record у self.data.
"""

from collections import UserDict
dict = {}

class Field:
    def __init__(self, value):
        self.value = value

class Name(Field):
    ...

class Phone(Field):
    ...

class Record:

    def __init__(self, name, phone=None):
        self.name = name
        self.phones = []

        if phone:
            self.add_phone(phone)

    def add_phone(self, phone):
        self.phones.append(phone)

    def change_phone(self, phone, new_tel):
        for i, phone in enumerate(self.phones):
            if self.phones[i].value == phone.value:
                self.phones[i] = new_tel

    def remove_phone(self, phone):
        for i, phone in enumerate(self.phones):
            if phone.value == phone.value:
                self.phones.pop(i)


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record




if __name__ == '__main__':
    print('Перевірка роботи класу Record')
    name1 = Name('Антуан Йосипович')
    tel1 = Phone('+380970000000')
    record = Record(name1, tel1)
    record.change_phone(tel1, Phone('+38(098)111 11 11'))
    record.add_phone(Phone('+380973333333'))
    print(record.name.value)
    print(record.phones[0].value)
    print(record.phones[1].value)
    print('----------------------------------------------------')
    print('перевірка роботи класу Addressbook')
    book1 = AddressBook()
    book1.add_record(record)
    #print(book1)
    for x in book1.data['Антуан Йосипович'].phones:
        print(x.value)
    for y in book1.data:
        print(y)
    print('----------------------------------------------------')
    print('Перевірка додавання наступних даних')
    name2 = Name('Стефанія')
    tel2 = Phone('0984556200')
    record2 = Record(name2, tel2)
    record2.add_phone(Phone('050-111-11-11'))
    book1.add_record(record2)
    #print(book1.data)
    for i in book1.data['Стефанія'].phones:
        print(i.value)
    for n in book1.data:
        print(n)