print("Welcome to python pizza deliveries!")
size = str(input("What size pizza do you want? S, M or L?\n"))
add_pepperoni = str(input("Do you want pepperoni? Y or N\n"))
extra_cheese = str(input("Do you want extra cheese? Y or N\n"))
bill = 0
if size == 'S':
    bill+= 15
elif size =='M':
    bill+= 20
else:
    print("Invalid input!")
if add_pepperoni == 'Y':
    if size == 'S':
        bill+=2
    else:
        bill+=3
if extra_cheese == 'Y':
    bill+=1
print("Your Final bill is: $",bill)