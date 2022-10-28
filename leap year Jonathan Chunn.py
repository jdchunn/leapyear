
# if year is evenly divisible by 4, divide year by 100. 
# if year is not evenly divisble by 4, year is not a leap year.
# if year is evenly divisible by 100, divide year by 400.
# if year is not evenly divisible by 100, year is a leap year.
# if year is evenly divisible by 400, year is a leap year.
# if year is not evenly divisible by 400, year is not a leap year.

year=1996

year_divisible_by_4=year%4
year_divisible_by_100=year%100
year_divisible_by_400=year%400

if (year_divisible_by_4) == 0:
    if (year_divisible_by_100) == 0:
        if (year_divisible_by_400) == 0:
            print(year, "is a leap year")
        if (year_divisible_by_400) != 0:
            print(year, "is not a leap year")
    if (year_divisible_by_100) != 0:
        print(year, "is a leap year")
if (year_divisible_by_4) != 0:
    print(year, "is not a leap year")















