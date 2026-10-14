class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def set_account_number(self, account_number):
        self.__account_number = account_number

    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print("The balance must not be a negative number.")
            self.__balance = self.__balance

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

def main():
    account1 = BankAccount(12345, 1000)

    print("Account 1")
    print("Account Number: ", account1.get_account_number())
    print("Balance: ", account1.get_balance())
    print()
    print("Update balance to -100")
    account1.set_balance(-100)
    print("Account Number: ", account1.get_account_number())
    print("Balance: ", account1.get_balance())

main()
    