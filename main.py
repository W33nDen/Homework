from datetime import date, timedelta


def get_birthdays_per_week(users):
    today = date.today()
    next_week = today + timedelta(days=7)
    birthdays = {}

    for user in users:
        birthday_this_year = user["birthday"].replace(year=today.year)

        # Якщо день народження вже минув у цьому році, перевіряємо на наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Перевіряємо, чи день народження потрапляє в наступний тиждень
        if today <= birthday_this_year < next_week:
            day_of_week = birthday_this_year.strftime("%A")
            # Переносимо дні народження на найближчі робочі дні, якщо вони випадають на вихідні
            if day_of_week == "Saturday":
                day_of_week = "Monday"  # Переносимо на понеділок
            elif day_of_week == "Sunday":
                day_of_week = "Monday"  # Переносимо на понеділок

            if day_of_week not in birthdays:
                birthdays[day_of_week] = []
            birthdays[day_of_week].append(user["name"])

    return birthdays


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
