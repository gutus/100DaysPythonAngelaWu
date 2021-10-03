
age = input("What is your current age?")


days_left = (90*365)-(int(age)*365)
weeks_left = (90*52)-(int(age)*52)
month_left = (90*12)-(int(age)*12)
print(
    f"You have {days_left} days, {weeks_left} weeks, and {month_left} months left")

print("ALTERNATIVE 2")
years_left = 90-int(age)
days_left2 = years_left*365
weeks_left2 = years_left*52
month_left2 = years_left*12
print(
    f"You have {days_left2} days, {weeks_left2} weeks, and {month_left2} months left")
