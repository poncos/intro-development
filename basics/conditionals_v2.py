from datetime import date

day = int(input("Please enter the day you were born? "))
month = int(input("Please enter the month you were born? "))
year = int(input("Please enter the year you were born? "))

now = date.today()
current_year = now.year
current_day = now.day
current_month = now.month

year_diff = current_year - year

if current_month > month:
    age = year_diff
elif current_month < month:
    age = year_diff -1
elif current_day < day:
    age = year_diff - 1
else:
    age = year_diff

print("Your age is " + str(age) + " years old.")
