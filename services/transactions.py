from utils.date_today import date_today

def deposit(account, value):
    # Does the deposit in the account.
    # Returns True if the deposit was successful, False otherwise.
    if value > 0:
        account.balance += value
        account.statement += (f"{date_today()} | DEPOSIT     | + $ {value:.2f}\n")
        print("Deposit made successfully!")
        return True
    else:
        print("Invalid deposit amount.")
        return False
    
def withdrawals(account, value):
    # Does the withdrawal from the account.
    # Returns True if the withdrawal was successful, False otherwise.
    if value > account.DAILY_LIMIT:
        print("Withdrawal exceeds the limit allowed per transaction.")
        return False
    if value > account.balance:
        print("Insufficient balance.")
        return False
    # Verify if the value is negative
    # If it is, return False
    if value < 0:
        print("Invalid withdrawal amount.")
        return False
    # If the value is valid, proceed with the withdrawal 
    else:
        account.balance -= value
        account.statement += (f"{date_today()} | WITHDRAWAL  | - $ {value:.2f}\n")
        account.number_withdrawals += 1
        print("Withdrawal made sucessfully!")
        return True