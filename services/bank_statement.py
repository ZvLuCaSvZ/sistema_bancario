def view_statement(account): 
    # Returns the bank statement of the account.
    print("\n============BANK STATEMENT============")
    print(account.statement if account.statement else "No bank transactions.")
    print(f"\aBalance: R$ {account.balance:.2f}")
    print("========================================")
    input("Press Enter to exit...")