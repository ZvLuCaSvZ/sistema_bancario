from utils.date_today import date_today

def reset_withdrawals(account):
    # Resets the number of withdrawals for the account at the start of a new day.
    # If the last withdrawal was made on a different day, reset the count.
    current_date = date_today()

    if account.last_withdrawals != current_date:
        account.number_withdrawals = 0
        account.last_withdrawals = current_date
    current_date = date_today()