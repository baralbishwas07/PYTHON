#head/tail generator using random module
import random 
choice = random .randint(0,1)
if choice == 0:
    print("Head")
else:
    print("Tail")