"""Assignment 3: Check whether a triangle is right-angled."""

def is_right_angled(s1, s2, s3):
    
	sides = [s1, s2, s3]
	sides.sort()

	return (sides[0] ** 2 + sides[1] ** 2) == sides[2] ** 2

print("Right-Angled Triangle Checker")

s1 = float(input("Enter the first side: "))
s2 = float(input("Enter the second side: "))
s3 = float(input("Enter the third side: "))

if s1 > 0 and s2 > 0 and s3 > 0:
	if is_right_angled(s1, s2, s3):
		print("The triangle is a right-angled triangle.")
	else:
		print("The triangle is not a right-angled triangle.")
else:
	print("Side lengths must be greater than zero.")

#OUTPUT
'''Right-Angled Triangle Checker
Enter the first side: 3
Enter the second side: 4
Enter the third side: 5
The triangle is a right-angled triangle.

Right-Angled Triangle Checker
Enter the first side: 1
Enter the second side: 2
Enter the third side: 3
The triangle is not a right-angled triangle.
'''