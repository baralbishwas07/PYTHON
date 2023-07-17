#This program will give a name of random person in the list who'll be paying the bill
import random
name_strings = input("Give me everybody's names, separated by comma\n")
name = name_strings.split(",")
total = len(name)
random_person = random.randint(0,total-1)
payer = name[random_person]
print(payer+" is going to buy the meal today!")