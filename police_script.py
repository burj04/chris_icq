fhand = open('test.txt')
for line in fhand:
    line_content = line.split()
    if 'yahooguy' in line:
        print("I don see am")
        print("It dey here : {0}".format(line))
    else:
        pass 

print("Completed")

"""
Assignment:
Write a program that will ask you the name of a file to read.
if the file is available, it should print the content the file 
if the file is not available it should handle the exception saying : 
    Please allow us more time to find the file.

"""