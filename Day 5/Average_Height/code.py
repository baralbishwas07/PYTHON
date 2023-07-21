sum = 0
n =0
list1 = input("Enter the list of elements:").split()
for i in range(0,len(list1)):
    list1[i] = int(list1[i])
    
for i in list1:
    n += 1

for i in list1:
    sum += i

average = sum/n
print("average:",average)