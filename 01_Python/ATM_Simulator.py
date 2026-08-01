print("=================")
print(" ATM Simulator ")
print("=================")
print("1. Check balance")
print("2. Deposit")
print("3. Withdraw")

balance = 1000000


options = int(input("Enter your choice: "))
if options == 1:
    print(f"Your balance is: {balance}")
elif options == 2:
    try:
        deposit = int(input("Enter amount to deposit: "))
        if deposit < 0:
            raise ValueError("Deposit amount cannot be negative!")
        balance += deposit
        print(f"Your new balance is: {balance}")
    except ValueError as e:
        print(e)
elif options == 3:
    try:
        withdraw = int(input("Enter amount to withdraw: "))
        if withdraw < 0:
            raise ValueError("Withdraw amount cannot be negative!")
        if withdraw > balance:
            raise ValueError("Insufficient funds!")
        balance -= withdraw
        print(f"Your new balance is: {balance}")
    except ValueError as e:
        print(e)
