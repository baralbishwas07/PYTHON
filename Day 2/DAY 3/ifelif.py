height = float(input("Enter your height:\n"))
if height>=120:
    print("You are eligible for a ride")
    age = int(input("Please Enter your age to continue\n"))
    if age<12:
        print("Please pay $ 5 ticket!")
    elif age<=18:
        print("Please pay $ 7 ticket !")
    else:
        print("Please pay $ 12 ticket!")
else:
    print("Sorry, You are not eligible for a ride")