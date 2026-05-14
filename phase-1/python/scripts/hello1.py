#This file is a modification of my "hello.py" file where we use 'def' to define our own function
#'def' simply, means define

def main():

	hello()
	name = input("what's your name?").title()
	hello(name)

def hello(to="specials"):
	print("hello ", to)
main()
