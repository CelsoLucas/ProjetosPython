balance = 0
def menu():
    print("=-="*15)
    print("Bank")
    print("=-="*15)
    print("1 - See Balence")
    print("2 - Deposit")
    print("3 - Withdraw")
    print("4 - Exit")

def show_balance():
    print(f"Your corrent balance is ${balance:.2f}")

def deposit():
    print(f"Your corrent balance is ${balance:.2f}")
    amount = float(input("Enter the amount you want to deposit: $"))
    if amount < 0:
        print("That's not a valid amount!")
        return 0
    else: 
        return amount

def withdraw():
    print(f"Your corrent balance is ${balance:.2f}")
    amount = float(input("Enter the amount you want to Withdraw: $"))
    if amount > balance:
        print("Insufficient founds")
        return 0
    elif amount < 0:
        print("Amount needs to be more than $0")
        return 0
    else: 
        return amount

while True:
    menu()
    option = int(input("Enter the option you want: "))
    print("=-="*15)

    if option == 1:
        show_balance()
    
    elif option == 2:
        balance += deposit()

    elif option == 3:
        balance -= withdraw()
    
    elif option ==  4:
        break

    else:
        print("Option not found! Try Again")