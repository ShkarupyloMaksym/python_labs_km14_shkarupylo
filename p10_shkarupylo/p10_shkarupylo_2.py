import numpy as np


def leap_year(full_years):
    return list(filter(lambda i: i % 400 == 0 or (i % 100 != 0 and i % 4 == 0), full_years))


def count_days(year, month, leap_year):
    global years
    if month == 2:
        if year in leap_year(years):
            return 29
        else:
            return 28
    elif month <= 7:
        if month % 2 == 0:
            return 30
        else:
            return 31
    else:
        if month % 2 == 0:
            return 31
        else:
            return 30


years = np.arange(1900, 2020 + 3, 1)
while True:
    year = input('Enter the year: (Integer from 1900 to 2022): ')
    if year.isdigit() and (int(year) in years):
        year = int(year)
        break
    print('Incorrect enter')

while True:
    month = input('Enter the num of month (Integer from 1 to 12): ')
    if month.isdigit() and (1 <= int(month) <= 12):
        month = int(month)
        break
    print('Incorrect enter')

print('Number of days in month:', count_days(year, month, leap_year))
