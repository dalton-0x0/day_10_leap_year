def is_leap(year):
    """
    This function takes a year as an argument and returns True if the year is
    a leap year and False if the year is not a leap year.
    """

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap year")
                return True
            else:
                print("Not leap year")
                return False
        else:
            print("Leap year")
            return True
    else:
        print("Not leap year")
        return False


def days_in_month(year, month):
    """
    This function takes a year and a month as arguments and returns the number
    of days in the month.
    """

    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_leap(year) and month == 2:
        return 29
    return month_days[month - 1]


year_input = int(input("Enter a year: "))
month_input = int(input("Enter a month: "))
days = days_in_month(year_input, month_input)
print("Number of days: ", days)
