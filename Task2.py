"""
Task 2
Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.

"""
data1=input("Enter text to write to the file:")
with open("Output.txt","w") as Y:
    Y.write(data1 +"\n")
    print("Data successfully written to output.txt. ")
print("\n")
data=input("Enter additional text to append:")
with open("Output.txt","a") as Y:
    Y.write(data)
    print("Data successfully appended.")
print("\n")
print("Final content of output.txt")
with open("Output.txt","r") as Y:
    for line in Y:
        print(f"{line.strip()}")