student_scores = input("Enter the marks of the students:").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
max = 0
for i in student_scores:
    if i > max:
     max = i
print("The highest score in the class is :",max)
