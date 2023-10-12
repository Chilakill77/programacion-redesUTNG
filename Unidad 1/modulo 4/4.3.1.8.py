#Kevin
def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, "->", end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido")
def days_in_month(year, month):
#Kevin
def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def days_in_month(year, month):
    if month < 1 or month > 12:
        return None
    
    days_per_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if is_year_leap(year):
        days_per_month[2] = 29
    
    return days_per_month[month]

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido")

def day_of_year(year, month, day):
  if month < 1 or month > 12 or day < 1 or day > days_in_month(year, month):
        return None
    
    days_in_previous_months = sum(days_in_month(year, m) for m in range(1, month))
    return days_in_previous_months + day

# Pruebas
print(day_of_year(2000, 12, 31))  
print(day_of_year(2023, 10, 11))  
print(day_of_year(1999, 2, 29))

