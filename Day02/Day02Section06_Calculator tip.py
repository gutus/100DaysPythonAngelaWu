### Tip Calculator
print("Welcome to Tip Calculator")
bill = int(input("How much the bill? \t"))
people = int(input("How many people to split?\t "))
tip = int(input("How many percent tip, 10%, 12% or 15% ?\t "))
each_person = ((bill/people) * (tip/100)) + (bill/people)
print(f"So each person pays {each_person}")
