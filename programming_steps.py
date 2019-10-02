"""
Write a program to ask you to enter the name of a file to read.
If the file exists, it should print the content of the file.
If the file is not available, it should handle the exception saying:
please allow us more time to find the file

steps
ask for filename
check if file exists
if file exists
  print the content
else if the file does not exist
  handle exception saying allow more time to look for the file
"""
filename = input("Pleas enter file name in .txt: ")
try:
    fhandle = print(open('filename'))
    """Now write the part of the program to print the file content in
    a situation the file is found
    """
except FileNotFoundError:
    print("File not found. Please allow us more time to find the file")
else:
    print("Program execution completed")
