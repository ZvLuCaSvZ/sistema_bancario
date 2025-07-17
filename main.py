from bank.menu import menu
from bank.account import Account
from services import transactions, bank_statement
from utils.clear_screen import clear_screen
from utils.daily_reset_withdrawals import reset_withdrawals
import time

def main():
    account = Account()
    while True:
        clear_screen()
        option = menu()

        if option == '1':
            value = input("\nEnter the amount to deposit: $ ").replace(",", ".")
            try:
                value = float(value)
                result = transactions.deposit(account, value)
            except ValueError:
                print("Failed to perform the operation.")
            time.sleep(2)

        elif option == '2':
            reset_withdrawals(account)
            if account.number_withdrawals >= account.WITHDRAWALS_LIMIT:
                print(f"Daily withdrawal limit reached ({account.number_withdrawals}).")
                time.sleep(1)
                continue
            
            value = input("\nEnter the amount to be withdrawn: $ ").replace(",", ".")
            try:
                value = float(value)
                result = transactions.withdrawals(account, value)
            except ValueError:
                print("Failed to perform the operation.")
            time.sleep(2)

        elif option == '3':
            bank_statement.view_statement(account)

        elif option == '4':
            print("\nThank you for using our banking system!")
            print("Exiting the system...\n")
            break

        else:
            print("Operation not recognized. Please try again.")
            time.sleep(2)

if __name__ == "__main__":
    main()
