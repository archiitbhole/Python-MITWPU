"""Assignment 1: Operations on List, Tuple and Dictionary."""

def main():
	# A list is ordered, mutable, and allows duplicate values.
	numbers = [10, 20, 30, 20]
	print("LIST OPERATIONS")
	print("Original:", numbers)
	numbers.append(40)                 # add one item
	numbers.extend([50, 60])           # add multiple items
	numbers.insert(1, 15)              # insert at an index
	numbers.remove(20)                 # remove the first matching item
	removed = numbers.pop()            # remove and return the last item
	numbers.sort()                     # sort the list
	print("After append, extend, insert, remove, pop and sort:", numbers)
	print("Popped item:", removed)
	print("Count of 20:", numbers.count(20))
	print("Index of 30:", numbers.index(30))
	print("Length:", len(numbers))

	# A tuple is ordered and immutable.  It can be 'appended' only by
	# creating a new tuple through concatenation.
	values = (3, 1, 3, 2)
	print("\nTUPLE OPERATIONS")
	print("Original:", values)
	values = values + (4,)             # tuple append equivalent
	print("After concatenation:", values)
	print("Count of 3:", values.count(3))
	print("Index of 2:", values.index(2))
	print("Slice:", values[1:4])
	print("Length:", len(values))
	print("Minimum and maximum:", min(values), max(values))

	# A dictionary stores key-value pairs; keys are unique.
	student = {"name": "Aarav", "roll_no": 1, "course": "Python"}
	print("\nDICTIONARY OPERATIONS")
	print("Original:", student)
	student["year"] = 2025            # add a key-value pair
	student.update({"course": "Python Programming"})
	print("Keys:", list(student.keys()))
	print("Values:", list(student.values()))
	print("Items:", list(student.items()))
	print("Course:", student.get("course"))
	removed_value = student.pop("year")
	print("Removed year:", removed_value)
	print("After pop:", student)
	print("Contains 'name':", "name" in student)

	print("\nFAQ EXAMPLES")
	a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	print("Q1:", a[::2])
	sample = [1, 2, 3]
	init_tuple = ("Python",) * (len(sample) - sample[::-1][0])
	print("Q2:", init_tuple)


if __name__ == "__main__":
	main()

#OUTPUT
'''
LIST OPERATIONS
Original: [10, 20, 30, 20]
After append, extend, insert, remove, pop and sort: [10, 15, 20, 30, 40, 50]
Popped item: 60
Count of 20: 1
Index of 30: 3
Length: 6

TUPLE OPERATIONS
Original: (3, 1, 3, 2)
After concatenation: (3, 1, 3, 2, 4)
Count of 3: 2
Index of 2: 3
Slice: (1, 3, 2)
Length: 5
Minimum and maximum: 1 4

DICTIONARY OPERATIONS
Original: {'name': 'Aarav', 'roll_no': 1, 'course': 'Python'}
Keys: ['name', 'roll_no', 'course', 'year']
Values: ['Aarav', 1, 'Python Programming', 2025]
Items: [('name', 'Aarav'), ('roll_no', 1), ('course', 'Python Programming'), ('year', 2025)]
Course: Python Programming
Removed year: 2025
After pop: {'name': 'Aarav', 'roll_no': 1, 'course': 'Python Programming'}
Contains 'name': True

FAQ EXAMPLES
Q1: [1, 3, 5, 7, 9]
Q2: ()
'''