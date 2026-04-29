class Account:
    def __init__(self, name, acct_no):
        self.name = name
        self.acct_no = acct_no
        self.balance = 2000
    def withdraw(self, amount):
        self.balance = self.balance - amount
    def deposit(self, amount):
        self.balance = self.balance + amount
    def print_info(self):
        print(self.name)
        print(self.acct_no)
        print(self.balance)

accounts = {}
n = int(input("Enter the no. of persons: "))
for i in range(n):
    name = input("Enter the Name: ")
    account_no = int(input("Enter the Account No.: "))
    accounts[account_no] = Account(name, account_no)

Account_no = int(input("Enter the Account Number: "))
if Account_no in accounts:
    acc = accounts[Account_no]
    print("✅ Account Found! Account Exists.")

    cont = "y"
    while cont.lower() == "y":
        print("------------------------------MENU------------------------------------")
        print("1. WITHDRAW")
        print("2. DEPOSIT")
        print("3. PRINT INFORMATION")
        print("4. EXIT")
        choice = int(input("Enter The Choice: "))
        if choice == 1:
            amount_withdraw = int(input("Enter the Amount to Withdraw: "))
            if amount_withdraw > acc.balance:
                print("Amount Withdrawal Not Possible. Please Try Again Later!")
            else:
                acc.withdraw(amount_withdraw)
                print("Amount Withdrawal Successfull!!")
        elif choice == 2:
            amount_deposit = int(input("Enter the Amount to Deposit: "))
            if amount_deposit <= 0:
                print("Deposited Amount is Negative.Please Try Again!!")
            else:
                acc.deposit(amount_deposit)
                print("Your Money has Successfully got Deposited!")
        elif choice == 3:
            acc.print_info()
        elif choice == 4:
            break
        else:
            print("Invalid Choice!")
        
        cont = input("Do You Want To Continue? (y/n): ")
else:
    print("Account Not Found! Please Try Again!")