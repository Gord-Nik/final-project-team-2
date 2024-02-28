from collections import defaultdict, OrderedDict
from datetime import datetime

users = [
    {"name": "Anatoliy Podlivkin", "birthday": datetime(1999, 10, 28)},
    {"name": "Karina Romantseva", "birthday": datetime(1954, 2, 25)},
    {"name": "Philipp Muravyov", "birthday": datetime(1987, 2, 28)},
    {"name": "Nataliya Kiss", "birthday": datetime(1944, 2, 28)},
    {"name": "Pavel Syropov", "birthday": datetime(1996, 3, 1)},
    {"name": "Lika Puntsova", "birthday": datetime(1976, 3, 2)},
    {"name": "Liza Korovay", "birthday": datetime(2008, 2, 26)}
]


def get_birthdays_per_week(users: list):
    today = datetime.today().date()

    birthdays_per_week = defaultdict(list)

    for user in users:
        birthday = user["birthday"].date()

        next_birthday = birthday.replace(year=today.year + 1) \
            if birthday.replace(year=today.year) < today \
            else birthday.replace(year=today.year)

        if (next_birthday - today).days < 7:
            day_of_week = next_birthday.strftime("%A")
            if day_of_week in ["Saturday", "Sunday"]:
                day_of_week = "Monday"
            birthdays_per_week[day_of_week].append(user["name"])

    ordered_birthdays = OrderedDict(
        (day, birthdays_per_week[day])
        for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    )

    for day, names in ordered_birthdays.items():
        if names:
            print(f"{day}: {', '.join(names)}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_birthdays_per_week(users)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
