# agr calculator
#tale the age 
c_age = int(input("What is your current age? \n"))
age = 90 - c_age
month = age*12
week = age*52
days = month*30
hour = days*24

# print("Your passing months are : " + str(month))
# print("Your passing week are : " + str(week))
# print("Your passing days are : " + str(days))
# print("Your passing hours are : " + str(hour))

result = f"You have {month} months, {week} weeks, {days} days and {hour} hours"

print(result)