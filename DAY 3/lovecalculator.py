name1 = input("What is your name?\n")
name2 = input("What is their name?\n")
combined_name = str(name1)+str(name2)
lower_case = combined_name.lower()
t = combined_name.count('t')
r = combined_name.count('r')
u = combined_name.count('u')
e = combined_name.count('e')

true = t + r + u + e

l = combined_name.count('l')
o = combined_name.count('o')
v = combined_name.count('v')
e = combined_name.count('e')

love = l + o + v + e

true_love = str(true) + str(love)
true_love = int(true_love)

if true_love <10 or true_love>90:
    print(f"Your score is {true_love},You go together like coke and mentos")
elif true_love>40 and true_love<50:
    print(f"Your score is {true_love},You are alright together")
else:
    print(f"Your score is {true_love}")