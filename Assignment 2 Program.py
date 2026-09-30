"""Assignment 2: Find the largest of three numbers."""

first = int(input("Enter the first integer: "))
second = int(input("Enter the second integer: "))
third = int(input("Enter the third integer: "))

if first >= second and first >= third:
	largest = first
elif not (second < first or second < third):
	largest = second
else:
	largest = third

print("The largest number is:", largest)

#OUTPUT
'''
Enter the first integer: 3
Enter the second integer: 4
Enter the third integer: 5
The largest number is: 5
'''