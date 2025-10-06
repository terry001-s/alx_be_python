# bank_account.py
# Defines the BankAccount class

class BankAccount:
    def __init__(self, initial_balance=0.0):
        """Initialize the bank account with an optional starting balance."""
        self.__account_balance = float(initial_balance)  # encapsulated attribute

    def deposit(self, amount):
        """Add money to the account."""
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money if sufficient balance is available."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if amount > self.__account_balance:
            return False
        self.__account_balance -= amount
        return True

    def display_balance(self):
        """Display the current balance."""
        print(f"Current Balance: ${self.__account_balance:.2f}")

    def get_balance(self):
        """Optional: Return the current balance (for testing)."""
        return self.__account_balance
