print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
opt1 = input("Would you like to go left or right?\n").lower()
if opt1 == 'left':
    opt2 = input("Would you like to swim or wait?\n").lower()
    if opt2 == 'wait':
        opt3 = input("Which door would you like to go? red,yellow,blue\n").lower()
        if opt3 == 'yellow':
            print("Congratulations You Win!")
        elif opt3 == 'red':
            print("you were burned by fire.\n Game Over.")
        elif opt3 == 'blue':
            print("You were eaten by beasts.\nGame Over.")
        else:
            print("Game Over")
    else:
        print("You were attacked by trout.\nGame Over")
else:
    print("You Fell into a hole.\nGame Over")