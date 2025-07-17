from datetime import datetime

def date_today():
    # Returns the current date formatted as "MM/DD/YYYY".
    return datetime.now().strftime("%m/%d/%Y")