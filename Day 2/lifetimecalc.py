#if you have 90 years life span calculate your remaining days in days,weeks and months
age = int(input("Enter your age:"))
days = (90-age) * 365
weeks = (90-age) * 52
months = (90-age) * 12
print(f"You have {days} days, {weeks} weeks, {months} months")