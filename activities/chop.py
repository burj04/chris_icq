cooking_items = ['rice', 'onions', 'salt', 'pepper', 'oil']

def chop_function(a_list):
    print(a_list)
    del a_list[0]  # remove the first element of  my list
    del a_list[3]
    print("I am inside a function now")


chop_function(cooking_items )
