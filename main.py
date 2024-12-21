from datetime import date, datetime


def get_birthdays_per_week(users):
    birthdays = {
        "monday": [],
        "tuesday": [],
        "wednesday": [],
        "thursday": [],
        "friday": [],
    }

    today = datetime.now().date()
    current_weekday = today.weekday()

    days_until_next_monday = (7 - current_weekday) % 7
    next_monday = today + days_until_next_monday
    next_friday = next_monday + datetime.timedelta(days=4)

    for user in users:
        birthday_this_year = user["birthday"].replace(year=today.year)
        if next_monday <= birthday_this_year <= next_friday:
            day_name = birthday_this_year.strftime("%A")
            birthdays[day_name].append(user["name"])
    return users


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
