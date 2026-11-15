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
        print("--Show Balance--")
    elif choice == "2":
        print("--Add Money--")
    elif choice == "3":
        print("--Withdraw Money--")
    elif choice == "4":
        print("--Exit--")
        break
    else:
        print("Invalid choice. Please try again.")