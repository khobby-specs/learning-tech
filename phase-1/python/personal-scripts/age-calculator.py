import datetime


months = [
    "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"
]
accept_form = "The accepted format is yyyy/mm/dd or day month, year. Eg. 1999/12/01 or 1st December,1999."

def main():
    month, day, year = get_date()
    check_age(year)

def get_date():
    print(accept_form)
    while True:    
        try:
            DOB = input("Enter Date Of Birth: ").strip()
            if "/" in DOB:
                year, MONTH, day = DOB.split("/")
                month = int(MONTH)
            elif "," in DOB:
                month_day, year = DOB.split(",")
                day, MONTH = month_day.split()

                month = months.index(MONTH) + 1
                
            else:
                raise ValueError
            return month, int(day), int(year)
        except (ValueError, IndexError):
            print("invalid format")

def check_age(x):
    current_time = datetime.datetime.now()
    yr = current_time.year
    Year = int(yr)

    age = Year - x
    print(age)


main()
