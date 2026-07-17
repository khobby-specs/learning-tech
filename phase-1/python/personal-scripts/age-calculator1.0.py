import datetime


months = [
    "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"
]
accept_form = "The accepted format is yyyy/mm/dd or day month, year. Eg. 1999/12/01 or 1st December,1999."

def main():
    month, day, year = get_date()#calling get_date() and assign variables to the values returned
    is_valid(month)
    check_age(year, month, day)

def get_date():
    print(accept_form)
    while True:    
        try:
            DOB = input("Enter Date Of Birth: ").strip().title()
            if "/" in DOB:
                year, MONTH, day = DOB.split("/")
                month = int(MONTH)
            elif "," in DOB:
                month_day, year = DOB.split(",")
                year = year.strip()
                day, MONTH = month_day.split()
                month = months.index(MONTH) + 1
                
            else:
                raise ValueError
            return month, int(day), int(year)
        except (ValueError, IndexError):
            print("invalid format")
def is_valid(x):
    while True:
        if not(x in months or 1 <= x <=12):
            DOB = input("Enter Date Of Birth: ").strip().title()
        else:
            pass
        break


def check_age(x, y, z):
    current_time = datetime.datetime.now()
    yr = current_time.year
    Month = current_time.month
    Day = current_time.day
    Year = int(yr)
    month_left = y - Month
    #if month_left > 0:
    months_live = 12 - month_left
    #elif month_left < 0:
    months_live1 = -1 * month_left
        
    if (y, z) > (Month, Day):
        age = Year - x
        """if month_left > 0:
            months_live = 12 - month_left
        elif month_left < 0:
            months_live = -1 * month_left"""
        r_age = age - 1
        print(f"Your are {r_age}year(s), {months_live}month(s) old")
    else:
        age = Year - x
        print(f"You are {age}year(s), {months_live1}months old")

main()
