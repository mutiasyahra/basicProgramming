class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount. Amount should be positive.")
            return
        self.balance += amount
        print(f"{amount} deposited successfully. Current balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount. Amount should be positive.")
            return
        if amount > self.balance:
            print("Insufficient balance to complete the withdrawal.")
            return
        self.balance -= amount
        print(f"{amount} withdrawn successfully. Current balance: {self.balance}")

    def check_balance(self):
        print(f"Current balance for {self.name}: {self.balance}")

def main():
    print("Welcome to the Banking System")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Exit")

    accounts = {}

    while True:
        try:
            option = int(input("Enter your option: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if option == 1:
            name = input("Enter account holder's name: ")
            if name in accounts:
                print("Account already exists for this name.")
            else:
                accounts[name] = BankAccount(name)
                print(f"Account created successfully for {name}.")

        elif option == 2:
            name = input("Enter account holder's name: ")
            if name not in accounts:
                print("Account not found for this name.")
            else:
                amount = float(input("Enter deposit amount: "))
                accounts[name].deposit(amount)

        elif option == 3:
            name = input("Enter account holder's name: ")
            if name not in accounts:
                print("Account not found for this name.")
            else:
                amount = float(input("Enter withdrawal amount: "))
                accounts[name].withdraw(amount)

        elif option == 4:
            name = input("Enter account holder's name: ")
            if name not in accounts:
                print("Account not found for this name.")
            else:
                accounts[name].check_balance()

        elif option == 5:
            print("Thank you for using the Banking System. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()