'''this menu bookinf application will allow the user
to book or order a mill by choosing options fro 1 - 6
'''
#this print functions provides directives for the user to make a choise
print (" Welcome to NIIT Python Resturant")
print (" *Your satisfaction is our concern*")
print("")
print ("choose .1. for Jellof Rice & Chicken @ N2000: ")
print ("choose .2. for grilled Yam @ N800: ")
print ("choose .3. Piza with two bottles of mineral @ N3000 : ")
print ("Choose .4. Ice cream with chocolate Flavor @ N1600: ")
print ("choose .5. Meat pie Premiun pack @ N500: ")
print ("choose .6. Pop corn Exclusive @ N500: ")
print ("choose .0. to Exit ")
print("")


try:
    
    
    selection = int(input("Enter a choise: "))
    selection < 7
    if selection == 1:
        print("")
        print (" Jellof Rice & Chicken Order was successful, thanks ")
        print("")
        #break
    if selection == 2:
        print("Grilled Yam order was successful, thanks")
        print("")
        #break
    if selection == 3:
        print("")
        print("Piza with two bottles of mineral order was successful, thanks")
            #break
    if selection == 4:
        print ("Piza with two bottles of mineral order was successful, thanks")
        print("")
            #break
    if selection == 5:
        print("")
        print("Meat pie Premiun pack order was successful, thanks")
            #break
    if selection == 6:
        print("")
        print ("Pop corn Exclusive order was successful, thanks")
            #break
    if selection == 0:
        exit
      
except ValueError:
    print ("Invalide choise, Enter numbers from 0-6 to order a food")
