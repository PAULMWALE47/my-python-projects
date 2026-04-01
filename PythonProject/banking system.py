def show_balance():
    print("Your current balance is $" + str(balance))
def deposit():
    amount = float(input("Enter the amount to be deposited: "))
    if amount <= 0:
        print("That's not a valid amount")
        return 0
    else:
        return amount

def withdraw():
    amount = float(input("Enter the amount to be withdrawn: "))
    if amount <= 0:
        print("The amount cannot be negative")
        return 0
    elif amount > balance:
        print("insufficient funds")
        return 0
    else:
        return amount



balance = 0
is_running = True

while is_running:
    print("Welcome to Banking System")
    print("1. show balance")
    print("2. deposit")
    print("3. withdraw")
    print("4. exit")
    choice = int(input("Enter a choice (1-4)"))

    if choice == 1:
        show_balance()
    elif choice == 2:
        balance += deposit()
    elif choice == 3:
        balance -= withdraw()
    elif choice == 4:
        is_running = False
    else:
        print ("invalid option")
        continue
print("Thank you for using Banking System")