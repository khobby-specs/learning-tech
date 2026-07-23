#Requirements: this script comes with a 3rd party module.
#To install it, please run 'pip install pyfiglet' in your virtual environment or terminal.
from email_validator import validate_email, EmailNotValidError
import csv
import os
import pyfiglet


CSV_FILE = "tested_mails.csv"
welcome = pyfiglet.figlet_format("--- Welcome to email validator --- ", font='digital')
print(welcome)
print("--- To exit, press ctrl+D\n")

if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Email"])

while True:
    try:
        name = input("Enter Name: ")
        email = input("Enter Email: ")
        validated_mail = validate_email(email, check_deliverability=False)
        normalized_email = validated_mail.normalized
        print()
        print(f"✅ {normalized_email} is valid")
        with open(CSV_FILE, mode="a") as file:
            writer = csv.writer(file)
            writer.writerow([name, normalized_email])
    except EOFError:
        exit = pyfiglet.figlet_format("--- Program exited --- ", font='digital')
        print(f"\n{exit}")
        break
    except EmailNotValidError:
        print()
        print("Email not valid")
        continue
        

