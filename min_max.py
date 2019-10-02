smallest = None
for itervar in [41, 12,3, 20, 2, 9, 74, 15, 1]:
    if smallest is None or itervar < smallest:
        print("Current values before: smallest = {0} itervar = {1}".format(smallest, itervar))
        smallest = itervar
        print("Current values after: smallest = {0} itervar = {1}".format(smallest, itervar))

print("Smallest : {0}".format(smallest))

"""For sqlite python tutorial goto
https://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html
"""
