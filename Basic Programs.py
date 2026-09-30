""" BASIC PROGRAMS """

# 1. Print Hello, World!
print("Hello, World!")


# 2. Find the largest of three numbers
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))
if number1 >= number2 and number1 >= number3:
	print("Largest number:", number1)
elif number2 >= number1 and number2 >= number3:
	print("Largest number:", number2)
else:
	print("Largest number:", number3)


# 3. Find the sum of two numbers
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
print("Sum:", number1 + number2)


# 4. Check whether a number is even or odd
number = int(input("Enter a number: "))
if number % 2 == 0:
	print("Even number")
else:
	print("Odd number")


# 5. Simple calculator
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")
if operator == "+":
	print("Answer:", number1 + number2)
elif operator == "-":
	print("Answer:", number1 - number2)
elif operator == "*":
	print("Answer:", number1 * number2)
elif operator == "/":
	if number2 != 0:
		print("Answer:", number1 / number2)
	else:
		print("Cannot divide by zero")
else:
	print("Invalid operator")


# 6. Check whether a number is positive, negative, or zero
number = float(input("Enter a number: "))
if number > 0:
	print("Positive")
elif number < 0:
	print("Negative")
else:
	print("Zero")


# 7. Find the sum of all digits of a number
number = int(input("Enter a number: "))
number = abs(number)
digit_sum = 0
while number > 0:
	digit_sum = digit_sum + number % 10
	number = number // 10
print("Sum of digits:", digit_sum)


# 8. Find the factorial of a number
number = int(input("Enter a non-negative number: "))
factorial = 1
for value in range(1, number + 1):
	factorial = factorial * value
print("Factorial:", factorial)


# 9. Check whether a number is prime
number = int(input("Enter a number: "))
is_prime = True
if number < 2:
	is_prime = False
else:
	for value in range(2, number):
		if number % value == 0:
			is_prime = False
			break
if is_prime:
	print("Prime number")
else:
	print("Not a prime number")


# 10. Print prime numbers from 10 to 99
for number in range(10, 100):
	is_prime = True
	for value in range(2, number):
		if number % value == 0:
			is_prime = False
			break
	if is_prime:
		print(number)


# 11. Accept 5 numbers and display their cube values
for count in range(5):
	number = int(input("Enter a number: "))
	print("Cube:", number ** 3)


# 12. Reverse a given number
number = int(input("Enter a number: "))
reverse = 0
while number > 0:
	reverse = reverse * 10 + number % 10
	number = number // 10
print("Reversed number:", reverse)


# 13. Check whether a year is a leap year
year = int(input("Enter a year: "))
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
	print("Leap year")
else:
	print("Not a leap year")


# 14. Display grade according to marks
marks = int(input("Enter marks in Math: "))
if marks >= 90 and marks <= 100:
	print("Grade: O")
elif marks >= 80 and marks <= 89:
	print("Grade: A+")
elif marks >= 70 and marks <= 79:
	print("Grade: A")
elif marks >= 60 and marks <= 69:
	print("Grade: B")
elif marks >= 50 and marks <= 59:
	print("Grade: C")
elif marks >= 40 and marks <= 49:
	print("Grade: P")
else:
	print("Grade: F")


# 16. Calculate percentage and display highest and lowest subject marks
student_name = input("Enter student name: ")
roll_number = input("Enter roll number: ")
math_marks = float(input("Enter Math marks: "))
science_marks = float(input("Enter Science marks: "))
english_marks = float(input("Enter English marks: "))
total = math_marks + science_marks + english_marks
percentage = total / 3
print("Student Name:", student_name)
print("Roll Number:", roll_number)
print("Percentage:", percentage)
if math_marks >= science_marks and math_marks >= english_marks:
	print("Highest: Math")
elif science_marks >= math_marks and science_marks >= english_marks:
	print("Highest: Science")
else:
	print("Highest: English")
if math_marks <= science_marks and math_marks <= english_marks:
	print("Lowest: Math")
elif science_marks <= math_marks and science_marks <= english_marks:
	print("Lowest: Science")
else:
	print("Lowest: English")
