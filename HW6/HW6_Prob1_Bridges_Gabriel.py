# Intro. Exp. Physics II HW5, Gabriel Bridges
# Problem 4.1
# GLB300@nyu.edu

days = {"january":31,"february":28,"march":31,"april":30,"may":31,"june":30,"july":31,"august":31,"september":30,"october":31,"november":30,"december":31}
cash = float(raw_input("How much money is in your lunch accout? "))
currentDay = int(raw_input("What day of the month is it today? "))-1
daysLeft = days[raw_input("what month is it? ").lower()]-currentDay
print("You can spend ${0:0.2f} per day" .format(cash/daysLeft))
