print("Wallet App")
assets = {}
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
    print("4-)Add Assets")
    print()
    print("5-)Exit")
    print()

def add_assets(assets):
    print("--Add Assets--")
    assets_name = input("Enter assets name: ").strip().upper()
    if not assets_name:
        print("Asset name cannot be empty.")
        return assets
    try:
        assets_amount = float(input("Enter the assets amount: "))
        if assets_amount <= 0:
            print("Amount must be greater than 0.")
            return assets
    except ValueError:
        print("Please enter a valid number for amount.")
        return assets
    try:
        assets_buy_price = float(input("Enter the buy price: "))
        if assets_buy_price <= 0:
            print("Buy price must be greater than 0.")
            return assets
    except ValueError:
        print("Please enter a valid number for buy price.")
        return assets

    if assets_name in assets:
        assets[assets_name]["buy price"] = ((assets[assets_name]["buy price"] * assets[assets_name]["amount"]) + (assets_buy_price * assets_amount)) / (assets[assets_name]["amount"] + assets_amount)
        assets[assets_name]["amount"] += assets_amount
    else:
        assets[assets_name] = {"amount" : assets_amount, "buy price": assets_buy_price}
    
    return assets

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
        assets = add_assets(assets)
        print(assets)
    elif choice == "5":
        print()
        print("--Exit--")
        break
    else:
        print("Invalid choice. Please try again.")