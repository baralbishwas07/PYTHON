#BMI = Weight/height^2
weight = int(input("Enter your Weight in kg:\n"))
height = float(input("Enter your Height in m:\n"))
BMI = weight/height ** 2
print("Your Body Mass Index(BMI) is:",round(BMI,2))