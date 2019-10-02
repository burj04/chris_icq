print("Welcome To My GApplication")
day_time = input("What time is it? :")

"""
remember :
x = x + 2
    ===>
day_time = float(day_time)
"""

day_time = float(day_time)

#check time is from 12am to 11.59 am
if (day_time >= 00.00 and day_time <= 11.59):
    print("Good morning Sir / Madam ")
elif (day_time >= 12.00 and day_time <= 15.59):
    print("Good afternoon Sir / Madam ")
elif (day_time >= 16.00 and day_time <= 18.59):
    print("Good evening Sir / Madam ")
elif(day_time >= 19.00 and day_time <= 23.59):
    print('Good night Sir / Madam')
else:
    print("Please I no understand you o :")
