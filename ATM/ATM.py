balance = 1000
PIN = "123456"

entered_pin = input("Enter your PIN: ")

if entered_pin != PIN:
    print("❌ Incorrect PIN. Access denied.")
    exit()

while True:
    print("\n🏧 ATM MENU")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        print(f"💰 Your balance is: ${balance}")

    elif choice == "2":
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            balance += amount
            print("✅ Deposit successful")
        else:
            print("❌ Invalid amount")

    elif choice == "3":
        amount = float(input("Enter amount to withdraw: "))
        if amount <= balance and amount > 0:
            balance -= amount
            print("✅ Withdrawal successful")
        else:
            print("❌ Insufficient balance or invalid amount")

    elif choice == "4":
        print("👋 Thank you for using the ATM")
        break

    else:
        print("❌ Invalid choice")
