"""Assignment 5: To check if string contains only alphabets and digits or it also has special characters."""
import re
string = input("Enter a string: ")
if re.fullmatch(r'[a-z A-Z 0-9]+', string):
    print("String contains only a-z, A-Z and 0-9.")
else:
    print("String contains Special characters.")

#OUTPUT
'''
Enter a string: Archit Bhole 1011
String contains only a-z, A-Z and 0-9.

Enter a string: Archit@MITWPU
String contains Special characters.
'''