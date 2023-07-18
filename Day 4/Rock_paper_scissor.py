import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock,paper,scissors]
option = int(input("what do you choose? Type 0 for Rock,1 for Paper or 2 for Scissors"))
if option >=3 or option < 0:
    print("Please type valid number as input!")
else:
    choice = random.randint(0,2)
    print(game_images[option])
    print("Computer chooses\n")
    print(game_images[choice]) 

    
    if option == 0 and choice == 2:
        print("You Win!")
    elif option == 2 and choice == 0:
        print("You Loose!")
    elif option > choice :
        print("You Win!")
    elif option < choice:
        print("You Loose!")
    elif option == choice:
        print("Draw!")
