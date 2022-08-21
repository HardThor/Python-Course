"""Завдання​

Вам треба реалізувати корисну функцію для виведення списку колег, яких потрібно привітати з днем народження на тижні.

У вас є список словників users, кожен словник у ньому обов'язково має ключі name та birthday. Така структура представляє 

модель списку користувачів з їх іменами і днями народження. name — це рядок з ім'ям користувача, а birthday — це datetime об'єкт,

в якому записаний день народження.

Ваше завдання написати функцію get_birthdays_per_week, яка отримує на вхід список users і виводить у консоль (за допомогою print) 

список користувачів, яких потрібно привітати по днях."""


from datetime import datetime, timedelta

users = [
    {"name": "Vladyslav", "birthday": "22 May 1990"},
    {"name": "Stephanie", "birthday": "24 August 1991"},
    {"name": "Ludmila", "birthday": "16 May 1990"},
    {"name": "Vasyl", "birthday": "28 August 1965"},
]


def get_birthdays_per_week(users):
    weekday = {
        'Monday': '',
        'Tuesday': '',
        'Wednesday': '',
        'Thursday': '',
        'Friday': '',
        'Next Monday': ''
        }
    start = datetime.now().date()
    end = start + timedelta(days=7)
    for i in users:
        birthday = datetime.strptime(i["birthday"], "%d %B %Y")
        date_b = datetime(start.year, birthday.month, birthday.day)
        if start <= date_b.date() <= end:
            day = date_b.weekday()
            if day == 0:
                weekday['Monday'] += i['name']
                weekday['Monday'] += ', '
            if day == 1:
                weekday['Tuesday'] += i['name']
                weekday['Tuesday'] += ', '
            if day == 2:
                weekday['Wednesday'] += i['name']
                weekday['Wednesday'] += ', '
            if day == 3:
                weekday['Thursday'] += i['name']
                weekday['Thursday'] += ', '
            if day == 4:
                weekday['Friday'] += i['name']
                weekday['Friday'] += ', '
            if day in (5, 6):
                weekday['Next Monday'] += i['name']
                weekday['Next Monday'] += ', '

    for k, v in weekday.items():
        count = 0
        if len(v) > 0:
            print(k + ': ' + v[:-2])
        else:
            count += 1
    if count > 0:
        print("No birthday in this week")


get_birthdays_per_week(users)