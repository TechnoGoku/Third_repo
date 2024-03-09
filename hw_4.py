from datetime import datetime, timedelta


users_list = [
    {"name": "Joe McNuggets", "birthday": "1985.03.15"},
    {"name": "Frensis McChicken", "birthday": "1990.01.09"},
    {"name": "Gustav Antonio", "birthday": "1990.03.05"},
    {"name": "Carl Johnson", "birthday":"1968.07.10"},
    {"name": "Nico Bellic", "birthday": "1990.03.09"},
    {"name": "Gabe Newell", "birthday": "1962.03.16"},
    {"name": "Sir Potato", "birthday": "2000.07.16"},
    {"name": "Mister Incognito", "brithday": "1999.03.12"}
]

def get_upcoming_birthdays(users):
    prepared_users = []
    for users in users_list:
        try:
            birthday_date = datetime.strftime(users_list["birthday"], "%Y.%m.%d").date
            prepared_users.append({"name": users["name"], "birthday": birthday_date})
        except:
            print(f'Некоректна дата народження для користувача {users["name"]}')
        return prepared_users
    print(prepared_users)
    print(birthday_date)


def find_next_weekday(d, weekday: int):  # Функція для знаходження наступного заданого дня тижня після заданої дати
    """
     Ф-ція для знаходження наступного заданого дня тижня після заданої дати
    :param d: datetime.date - початкова дата
    :param weekday: int - день тижня від 0 (понеділок) до 6 (неділя)
    :return:
    """
    days_ahead = weekday - d.weekday()  # Різниця між заданим днем тижня та днем тижня заданої дати
    if days_ahead <= 0:  # Якщо день народження вже минув
        days_ahead += 7  # Додаємо 7 днів, щоб отримати наступний тиждень
    return d + timedelta(days=days_ahead)  # Повертаємо нову дату


    

get_upcoming_birthdays(users_list)
today = datetime.today().date()

print(today)
print(users_list)