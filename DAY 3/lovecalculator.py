name1 = input("What is your name?\n")
name2 = input("What is their name?\n")
combined_name = str(name1)+str(name2)
lower_case = combined_name.lower()
t = lower_case.count('t')
r = lower_case.count('r')
u = lower_case.count('u')
e = lower_case.count('e')


true = t + r + u + e

l = lower_case.count('l')
o = lower_case.count('o')
v = lower_case.count('v')
e = lower_case.count('e')

love = l + o + v + e

true_love = str(true) + str(love)
print(true_love)
true_love = int(true_love)

if true_love <10 or true_love>90:
    print(f"Your score is {true_love},You go together like coke and mentos")
elif true_love>40 and true_love<50:
    print(f"Your score is {true_love},You are alright together")
else:
    print(f"Your score is {true_love}")