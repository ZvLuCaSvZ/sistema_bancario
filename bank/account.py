class Account:
    def __init__(self):
        self.balance = 0.0
        self.statement  = ""
        self.number_withdrawals = 0
        self.last_withdrawals = None
        self.WITHDRAWALS_LIMIT = 3
        self.DAILY_LIMIT = 500.0