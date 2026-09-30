"""List Programs - 18 independent basic programs."""

# 1. Create a list of 5 integers, display it, and access elements by index.
numbers = [10, 20, 30, 40, 50]
print(numbers)
for index in range(len(numbers)):
	print("Index", index, ":", numbers[index])


# 2. Append a new item to the end of a list.
numbers = [1, 2, 3, 4]
numbers.append(5)
print(numbers)


# 3. Reverse the order of items in a list.
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)


# 4. Print the number of occurrences of a specified element.
numbers = [1, 2, 3, 2, 4, 2, 5]
element = int(input("Enter an element: "))
print("Occurrences:", numbers.count(element))


# 5. Append the items of list1 to list2 in the front.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list2 = list1 + list2
print(list2)


# 6. Insert a new item before the second element.
numbers = [10, 20, 30, 40]
numbers.insert(1, 15)
print(numbers)


# 7. Remove the item from a specified index.
numbers = [10, 20, 30, 40, 50]
index = int(input("Enter index to remove: "))
if 0 <= index < len(numbers):
	numbers.pop(index)
print(numbers)


# 8. Remove the first occurrence of a specified element.
numbers = [10, 20, 30, 20, 40]
element = int(input("Enter element to remove: "))
if element in numbers:
	numbers.remove(element)
print(numbers)


# 9. Accept 20 values and count similar, even/odd, and positive/negative values.
numbers = [int(input("Enter value: ")) for _ in range(20)]
print("Repeated values and their indexes:")
for value in set(numbers):
	indexes = [i for i, item in enumerate(numbers) if item == value]
	if len(indexes) > 1:
		print(value, "count =", len(indexes), "indexes =", indexes)
print("Even:", sum(value % 2 == 0 for value in numbers))
print("Odd:", sum(value % 2 != 0 for value in numbers))
print("Positive:", sum(value > 0 for value in numbers))
print("Negative:", sum(value < 0 for value in numbers))


# 10. Accept 10 values and perform sorting and length operations.
numbers = [int(input("Enter value: ")) for _ in range(10)]
print("Ascending:", sorted(numbers))
numbers.sort(reverse=True)
print("Descending:", numbers)
print("Length:", len(numbers))


# 11. Accept two lists and merge them using +.
list1 = input("Enter first list values: ").split()
list2 = input("Enter second list values: ").split()
merged = list1 + list2
print(merged)


# 12. Create an uppercase acronym from a phrase.
phrase = input("Enter a phrase: ")
acronym = "".join(word[0] for word in phrase.split()).upper()
print(acronym)


# 13. Print the abbreviation of a month given its number.
month_number = int(input("Enter month number (1-12): "))
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
if 1 <= month_number <= 12:
	print(months[month_number - 1])
else:
	print("Invalid month number")


# 14. Insert, delete, and display elements of a list.
numbers = [10, 20, 30]
numbers.insert(1, 15)
numbers.remove(30)
print(numbers)


# 15. Merge two lists into a dictionary.
keys = ["name", "age", "city"]
values = ["Alex", 20, "Pune"]
print(dict(zip(keys, values)))


# 16. Remove duplicate elements from a list.
numbers = [1, 2, 2, 3, 4, 3, 5, 1]
unique_numbers = []
for number in numbers:
	if number not in unique_numbers:
		unique_numbers.append(number)
print(unique_numbers)


# 17. Convert two lists into a dictionary using zip().
keys = ["a", "b", "c"]
values = [1, 2, 3]
dictionary = dict(zip(keys, values))
print(dictionary)


# 18. Find common elements in two lists.
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common = [item for item in list1 if item in list2]
print(common)
