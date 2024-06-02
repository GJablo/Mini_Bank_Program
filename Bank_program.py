# simple python banking program

def show_bal(balance):
    print("#############################")
    print(f"Your balance is Ksh.{balance:.2f}")
    print("#############################")

def deposit():
    print("#############################")
    amount = float(input("Enter an amount to be deposited: "))
    print("#############################")

    if amount < 0:
        print("#############################")
        print("That's not a valid amount!")
        print("#############################")
        return 0
    else:
        return amount

def withdraw(balance):
    print("#############################")
    amount = float(input("Enter amount to be withdrawn: "))
    print("#############################")

    if amount > balance:
        print("#############################")
        print("Insufficient funds!")
        print("#############################")
        return 0
    elif amount < 0:
        print("#############################")
        print("Please enter a valid amount!")
        print("#############################")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("#############################")
        print("Banking program")
        print("#############################")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("#############################")

        usr_choice = input("Enter your choice (1-4): ")

        if usr_choice == '1':
            show_bal(balance)
        elif usr_choice == '2':
            balance += deposit()
        elif usr_choice == '3':
            balance -= withdraw(balance)
        elif usr_choice == '4':
            is_running = False
        else:
            print("#############################")
            print("That is not a valid choice!")
            print("#############################")

    print("Thank you! Have a nice day!")

if __name__ == '__main__':
    main()