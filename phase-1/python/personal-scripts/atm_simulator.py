import sys
symbol = ["!", "@", "#", "$"]
def main():
    set_bal = set_acc_bal()
    acc_balance = set_bal
    print(f"Account Balance: ${acc_balance}")
    withdraw(acc_balance)
    
def set_acc_bal():
    while True:
        try:
            set_balance = input("Set Account Balance: ").strip()
            for char in set_balance:
                if char in symbol:
                    set_bal = set_balance.replace(char,"")
                    acc_balance = int(set_bal)
                    return acc_balance
                elif char not in symbol:
                    set_bal = int(set_balance)
                    return set_bal
        except(TypeError, ValueError):
            set_balance
    
def withdraw(money):
    while money > 0:
        try:
            amt_to_withdraw = input("Enter amount to withdraw: $")
            amt_to_withdraw_new = int(amt_to_withdraw)
            if amt_to_withdraw_new > money:
                print("Insufficient funds")
                print(f"Account Balance: ${money}")
                amt_to_withdraw
            else:
                money -= amt_to_withdraw_new
                print(f"Account Balance: ${money}")
        except (TypeError, ValueError):
            amt_to_withdraw
        except EOFError:
            print()
            sys.exit()
            
main()
