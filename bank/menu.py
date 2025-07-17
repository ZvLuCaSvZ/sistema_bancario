def menu():
    # View the banking menu.
    # Returns the option selected by the user.
    print("""
Welcome!
========================================
1 - DEPOSIT
2 - WITHDRAWN
3 - BALANCE
4 - EXIT
========================================""")
    option = input("Please, select a banking operation: ").strip()
    return option