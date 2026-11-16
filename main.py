print("Wallet App")
balance = 0
while True:
    print()
    print("1-)Show Balance")
    print()
    print("2-)Add Money")
    print()
    print("3-)Withdraw Money")
    print()
    print("4-)Exit")
    print()
    choice = input("Your Choice: ")
    if choice == "1":
        print()
        print("--Show Balance--")
        print(f"Your balance is: {balance:.2f}$")
    elif choice == "2":
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
    elif choice == "3":
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
                print(f"Your new balance {balance:.2f}$")
        except ValueError:
            print("Please enter a number.")

    elif choice == "4":
        print()
        print("--Exit--")
        break
    else:
        print("Invalid choice. Please try again.")