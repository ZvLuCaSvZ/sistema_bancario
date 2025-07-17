import os

def clear_screen():
    # Clear the console screen.
    # This works for both Windows and Unix-like systems.
    os.system('cls' if os.name == 'nt' else 'clear')