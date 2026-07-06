import random
import sys

welcome = "Welcome to the number guesing game."
note = "Note: You're to guess between numbers 1 - 10."

if len(sys.argv) > 2:
    print("You enterd too many command arguments")
    print(welcome)
    print(note)
    num_gen = random.randint(1,10)
    while True:
        try:
            guessed_num = int(input("Enter guess:"))
            if guessed_num > num_gen:
                print("opps!... Too high")
                guessed_num
            elif guessed_num < num_gen:
                print("opps!... Too low")
                guessed_num
            else:
                print("Congratulations, You guessed just right!")
                break
        except TypeError:
            print("Enter a valid number")
            guessed_num
        except EOFError:
            print()
            print("Exit successful")
            sys.exit()
            
elif len(sys.argv) == 2:
    num = sys.argv[1]
    number = int(num)
    print(welcome)
    print(note)
    num_gen = random.randint(1,10)
    while True:
        try:
            if number > num_gen:
                print("opps!... Too high")
                number = int(input("Enter guess: "))
            elif number < num_gen:
                print("opps!... Too low")
                number = int(input("Enter guess: "))
            else:
                print("Congratulations, You guessed just right!")
                break
        except TypeError:
            print("Enter a valid number")
            guessed_num
        except EOFError:
            print()
            print("Exit successful")
            sys.exit()
elif len(sys.argv) == 1:
    print(welcome)
    print(note)
    num_gen = random.randint(1,10)
    while True:
        try:
            guessed_num = int(input("Enter guess:"))
            if guessed_num > num_gen:
                print("opps!... Too high")
                guessed_num
            elif guessed_num < num_gen:
                print("opps!... Too low")
                guessed_num
            else:
                print("Congratulations, You guessed just right!")
                break
        except TypeError:
            print("Enter a valid number")
            guessed_num
        except EOFError:
            print()
            print("Exit successful")
            sys.exit()
