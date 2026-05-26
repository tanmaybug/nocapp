from datetime import datetime

def date_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def date_format(date_string):
    if not date_string:
        return ""

    try:
        return datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S").strftime("%d-%m-%Y")
    except (ValueError, TypeError):
        return ""