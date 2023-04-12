from datetime import datetime

def check_date():
    max_life_time = 50
    current_date = datetime.now()
    years = []
    for i in range(int(current_date.year)-max_life_time, int(current_date.year)+1):
        years.append(str(i))
    months = []
    for i in range(1, 13):
        months.append(str(i))
    days = []
    for i in range(1, 32):
        days.append(str(i))
    return [years, months, days]