from email_validator import validate_email, EmailNotValidError
import csv

CSV_FILE = "tested_mails.csv"
print("\n ---Welcome to email validator--- ")
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
        break
    except EmailNotValidError:
        print("Email not valid")
        continue
        
