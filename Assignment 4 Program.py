"""Assignment 4: Addition of two matrices using lists and NumPy."""

import numpy as np


def read_matrix(rows, columns, name):
	"""Read a matrix from the user and return it as a list of lists."""
	matrix = []
	print(f"Enter elements of {name} row by row:")
	for i in range(rows):
		while True:
			try:
				row = list(map(float, input(f"Row {i + 1}: ").split()))
				if len(row) != columns:
					raise ValueError
				matrix.append(row)
				break
			except ValueError:
				print(f"Please enter exactly {columns} numeric values.")
	return matrix


def display(matrix):
	for row in matrix:
		print(" ".join(f"{value:g}" for value in row))


def main():
	print("Matrix Addition")
	while True:
		try:
			rows = int(input("Enter number of rows: "))
			columns = int(input("Enter number of columns: "))
			if rows <= 0 or columns <= 0:
				raise ValueError
			break
		except ValueError:
			print("Rows and columns must be positive integers.")

	matrix_a = read_matrix(rows, columns, "Matrix A")
	matrix_b = read_matrix(rows, columns, "Matrix B")

	# Addition using Python lists (element-wise).
	list_sum = [
		[matrix_a[i][j] + matrix_b[i][j] for j in range(columns)]
		for i in range(rows)
	]

	# Addition using NumPy arrays.
	numpy_sum = np.array(matrix_a) + np.array(matrix_b)

	print("\nAddition using Python lists:")
	display(list_sum)
	print("\nAddition using NumPy arrays:")
	display(numpy_sum.tolist())


if __name__ == "__main__":
	main()

#OUTPUT
'''Matrix Addition
Enter number of rows:  3
Enter number of columns:  3
Enter elements of Matrix A row by row:
Row 1:  2 3 4
Row 2:  5 6 7
Row 3:  9 10 11
Enter elements of Matrix B row by row:
Row 1:  23 24 25
Row 2:  12 14 16
Row 3:  32 33 34

Addition using Python lists:
25 27 29
17 20 23
41 43 45

Addition using NumPy arrays:
25 27 29
17 20 23
41 43 45
'''
