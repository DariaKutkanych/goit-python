from datetime import date, timedelta, datetime as dt
import calendar
import random
import sys


def random_employee_list(num):

    NAMES_LIST = ['Oliver', 'Jake', 'Noah', 'James', 'Jack', 'Connor', 'Liam',
              'John', 'Harry', 'Callum', 'Mason', 'Robert', 'Jacob', 'Jacob',
              'Jacob', 'Michael5', 'Charlie', 'Kyle', 'William', 'William',
              'Thomas', 'Joe', 'Ethan', 'Davi', 'George', 'Reece', 'Michael',
              'Richard', 'Oscar', 'Rhys', 'Alexander', 'Amelia', 'Margaret',
              'Emma', 'Mary', 'Olivia', 'Bill', 'Gill', 'Nill']

    employee_list = []
    start = dt(year=1922, month=1, day=1)

    for _ in range(num):
        random.seed()
        date = (start + timedelta(days=(random.randint(0, 36500)))).date()
        name = random.choice(NAMES_LIST)
        employee_list.append({"name": name, "birthday": date})

    return employee_list


def get_birthdays_per_week(users):

    WORKING_FORTNIGHT_LIST = [0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
    today = date.today()
    one_week_interval = timedelta(weeks=1)
    new_year = today.replace(month=12, day=31)
    days_after_ny = timedelta(days=(today + one_week_interval - new_year).days) if today <= new_year < (
        today + one_week_interval) else timedelta(days=0)

    week_start = today.weekday() if today.weekday() not in [5, 6] else 0
    days_for_display = WORKING_FORTNIGHT_LIST[
        WORKING_FORTNIGHT_LIST.index(week_start):][:5]
    birthday_dict = dict.fromkeys(days_for_display, [])

    for employee in users:

        current_year = today.year

        if isinstance(employee["birthday"], str):
            bd_date = dt.strptime(employee["birthday"], "%Y-%m-%d").date()
        else:
            bd_date = employee["birthday"]

        # end of year check. 2000 is a leap year taken as a benchmark
        if (new_year.replace(year=1999) <
            bd_date.replace(year=2000) <
            (new_year.replace(year=1999) + days_after_ny)):

            current_year_bd_date = bd_date.replace(year=(current_year + 1))
        
        else:
            try:
                current_year_bd_date = bd_date.replace(year=current_year)
            except ValueError:  # for 29th Fabruary
                continue

        celebration_weekday = (current_year_bd_date.weekday() if
                               current_year_bd_date.weekday() not in [5, 6]
                               else 0)

        if today <= current_year_bd_date < (today + one_week_interval):

            birthday_dict[celebration_weekday] = (birthday_dict[celebration_weekday]
                                                  + [employee["name"]])
            # birthday_dict[celebration_weekday].append(employee["name"]) doesn't work (((

    for work_day in days_for_display:

        weekday_result = f'{calendar.day_name[work_day]}: {", ".join(birthday_dict.get(work_day))}'

        print(weekday_result)


if __name__ == "__main__":

    if len(sys.argv) > 1:
        get_birthdays_per_week(sys.argv[1])

    else:
        user_list = int(input("Please enter random employees amount(int): "))
        get_birthdays_per_week(random_employee_list(user_list))
