import datetime

def get_date():
    current_date = datetime.datetime.now()
    formatted_date = current_date.strftime("%a, %b %d")
    return formatted_date