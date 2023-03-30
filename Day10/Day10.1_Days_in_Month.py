def is_leap(selected_year):
  if selected_year % 4 == 0:
    if selected_year % 100 == 0:
      if selected_year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(selected_year, selected_month):
    if is_leap(selected_year) == True:
        month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return month_days[selected_month - 1]  
    else:
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
        return month_days[selected_month - 1]
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(selected_year=year, selected_month=month)
print(days)