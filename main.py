print("Wallet App")
balance = 0

def show_balance(balance):
    print()
    print("--Show Balance--")
    print(f"Your balance is: {balance:.2f}$")
    
def add_money(balance):
    print()
    print("--Add Money--")
    try:
        add_money_amount = float(input("Enter amount to add: "))
        if add_money_amount <= 0:
            print("Amount must be greater than 0.")
        else:
            balance += add_money_amount
            print(f"Your new balance is {balance:.2f}$")
    except ValueError:
        print("Please enter a number.")
    return balance

def withdraw_money(balance):
    print()
    print("--Withdraw Money--")
    try:
        withdraw_money_amount = float(input("Enter amount to withdraw: "))
        if withdraw_money_amount <= 0:
            print("Amount must be greater than 0.")
        elif withdraw_money_amount > balance:
            print("Insufficient balance.")
        else:
            balance -= withdraw_money_amount
            print(f"Your new balance is {balance:.2f}$")
    except ValueError:
        print("Please enter a number.")
    return balance

def show_menu():
    print()
    print("1-)Show Balance")
    print()
    print("2-)Add Money")
    print()
    print("3-)Withdraw Money")
    print()
    print("4-)Exit")
    print()

while True:
    show_menu()
    choice = input("Your Choice: ")
    if choice == "1":
       show_balance(balance)
    elif choice == "2":
       balance = add_money(balance)
    elif choice == "3":
        balance = withdraw_money(balance)
    elif choice == "4":
        print()
        print("--Exit--")
        break
    else:
        print("Invalid choice. Please try again.")