#BMI (Body Mass Index)
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
#BMI=weight/(height**2)
# **2 >> square
# **3 >> cubic

#Write your code below this line
bmi = weight/height ** 2
print(round(bmi, 1))
