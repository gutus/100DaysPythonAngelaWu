# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
lower_name1 = name1.lower()
lower_name2 = name2.lower()
total1 = lower_name1.count("t")+lower_name1.count("r")+lower_name1.count("u")+lower_name1.count(
    "e")+lower_name1.count("l")+lower_name1.count("o")+lower_name1.count("v")+lower_name1.count("e")
total2 = lower_name2.count("t")+lower_name2.count("r")+lower_name2.count("u")+lower_name2.count(
    "e")+lower_name2.count("l")+lower_name2.count("o")+lower_name2.count("v")+lower_name2.count("e")
love_score = int(total1) + int(total2)
if (love_score <= 10) or (love_score >= 90):
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) or (love_score <= 50):
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")
