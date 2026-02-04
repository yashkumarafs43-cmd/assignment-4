"""
Task 1: Read a File and Handle Errors
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.

"""
#let make a file first
line1="This is a sample text file.\n"
line2="It contains multiple lines.\n"
with open("sample.txt","wt") as Y:
    Y.write(line1)
    Y.write(line2)
try:
    with open("sample.txt","rt") as Y:
        print("Reading file content:")
        line_no=1
        for line in Y:
            print(f"Line{line_no}:{line.strip()}")
            line_no+=1
except FileNotFoundError:
    print("Error:The file 'sample.txt' was not found")