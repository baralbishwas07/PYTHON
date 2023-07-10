weight = float(input("Please Enter your weight in kg:\n"))
height = float(input("Enter your height in m:\n"))
BMI = weight/(height **2)
if BMI<18.5:
    print(f"Your BMI is {BMI} and you are underweight")
elif BMI>= 18.5:
    print(f"Your BMI is {BMI} and you are a normal weighted")
elif BMI>=25:
    print(f"Your BMI is {BMI} and you are slightly overweight")
elif BMI>=30:
    print(f"Your BMI is {BMI} and you are obese")
else:
    print(f"Your BMI is {BMI} and you are clinically obese")