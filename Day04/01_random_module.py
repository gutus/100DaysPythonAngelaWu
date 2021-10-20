#### Random Module ####
import random

# Integer number acak antara 1 hingga 3
random_Integer = random.randint(1, 3)

print(random_Integer)

# Float Number acak menggunakan random.random()
randomFloat = random.random() * 5
print(f"Ini adalah float number acak >>> {randomFloat}")


# Love score menggunakan integer random
loveScore = random.randint(1, 100)
if loveScore < 50:
    print(
        f"Your love score {loveScore} is too low now, please try again later!")
else:
    print(
        f"Congratulation your Love Score is {loveScore}, yo can go to the next level now!")
