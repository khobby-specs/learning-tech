#Creating a password streght checker with concepts understood from cs50P lectures(Week0,1 & 2)

#Ask user for input
"""creates a main function"""
def main():
	passwords = input("Enter password: \n")  # user enters "password" and the value is store under password
	suggest_pass = "DoggY_bIy3@fAm!!!"
	capital = check_capital(passwords) #my own function that would check if password contains capital
	number = check_num(passwords) #check if password contains number
	symbol = check_symbol(passwords) #checks if password contains symbols
	lower = check_lower(passwords)
	strength = int(capital+number+symbol+lower) # password strength score
	if len(passwords) >= 8:
		if strength == 5:
			print(f"Your password ({passwords}) is very strong")
		elif strength == 4:
			print(f"Your password ({passwords}) is strong")
		elif strength == 3:
			print(f"Your password ({passwords}) is okay")
		elif strength == 2:
			print(f"Your password ({passwords}) is weak")
		else:
			print(f"Your password ({passwords}) is very weak")
			print(f"Your password could be '{suggest_pass}'.")
	else:
		print("Password should be more than 8 characters")

def check_capital(passwords):
	if any(letters.isupper() for letters in passwords):
		capital = 2
	else:
		capital = 0
	return capital

def check_num(passwords):
	number = 0
	for letters in passwords:
		if letters.isdigit():
			number = 1
	return number

def check_lower(passwords):
	if any(letters.islower() for letters in passwords):
		lower = 1
	else:
		lower = 0
	return lower

def check_symbol(passwords):
	if any(not letters.isalnum() and not letters.isspace() for letters in passwords):
		return 1
	return 0

main()
