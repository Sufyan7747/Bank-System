# === GLOBAL STORAGE ===
accounts = {}      # Dictionary to store accounts using acc_id as key
id_list = []       # List to track already used account IDs
acc_counter = 0    # Optional: counts total accounts created

# === CLASS DEFINITION ===
class Bank:
    def __init__(self):
        self.acc_id = ""           # Account ID will be created from name + CNIC
        self.acc_name = ""         # Name of account holder
        self.acc_balance = 0.0     # Starting balance

    def new_acc(self):
        global acc_counter

        # Ask for name
        self.acc_name = input("Enter account-holder name: ")

        # Repeat until a unique, valid CNIC is given
        while True:
            NIC = input("Enter your CNIC number (14 digits): ")

            # Validate CNIC length
            if len(NIC) != 14 or not NIC.isdigit():
                print("Enter a valid CNIC number of 14 digits.")
                continue

            # Generate account ID from first 3 letters of name + 4 digits of CNIC
            self.acc_id = self.acc_name[:3].lower() + NIC[1:5]

            # Check if ID already exists
            if self.acc_id in id_list:
                print("Account already exists with this ID.")
            else:
                break   # valid and unique

        self.acc_balance = 0.0      # New accounts start with zero balance
        id_list.append(self.acc_id) # Track used ID
        accounts[self.acc_id] = self  # Save account object in global dict
        acc_counter += 1            # Increment total accounts

        print("Account created successfully.")
        print("Your account ID is:", self.acc_id)

    def deposit(self):
        try:
            deposit_value = float(input("Enter the value you want to deposit: "))
            if deposit_value <= 0:
                print("Deposit must be greater than 0.")
                return
            self.acc_balance += deposit_value
            print(f"Deposited: ${deposit_value:.2f}")
        except ValueError:
            print("Invalid amount. Please enter a number.")

    def withdraw(self):
        try:
            withdraw_value = float(input("Enter the value you want to withdraw: "))
            if withdraw_value <= 0:
                print("Withdraw value must be greater than 0.")
                return
            if withdraw_value <= self.acc_balance:
                self.acc_balance -= withdraw_value
                print(f"Withdrew: ${withdraw_value:.2f}")
            else:
                print("Cannot withdraw more than account balance.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def check_balance(self):
        print("Your Bank Balance is: $", self.acc_balance)

    def full_print(self):
        # Using your version of detailed printout
        print("\nAccount Details:")
        print("Name   :", self.acc_name)
        print("ID     :", self.acc_id)
        print("Balance:", self.acc_balance)

# === MAIN MENU ===
def main():
    while True:
        print("Menu")
        print("1: New Account")
        print("2: Deposit")
        print("3: Withdraw")
        print("4: Check Balance")
        print("5: Show Account Details")
        print("6: Exit")

        action = input("Enter the number for your action: ")

        match action:
            case "1":
                account = Bank()
                account.new_acc()

            case "2" | "3" | "4" | "5":
                acc_id = input("Enter your account ID: ")
                if acc_id not in accounts:
                    print("Account not found.")
                    continue
                account = accounts[acc_id]

                if action == "2":
                    account.deposit()
                elif action == "3":
                    account.withdraw()
                elif action == "4":
                    account.check_balance()
                elif action == "5":
                    account.full_print()

            case "6":
                print("Exiting. Thank you for using the bank system.")
                break

            case _:
                print("Invalid input. Choose a number from 1 to 6.")

# === RUN PROGRAM ===
main()
