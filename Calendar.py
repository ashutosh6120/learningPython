import calendar

year = int(input("enter the year of the calendar: "))
month = int(input("enter the month of the calendar: "))

#to display that particular month  
x = calendar.month(year,month)
print(x)

#to display the year which you want
Month = int(input("enter which year to be displayed for all months: "))
print(calendar.calendar(Month))