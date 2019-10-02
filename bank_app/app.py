'''
check_bal
transfer_fund
open_account
withdraw
'''
import math
name  = ''
telephone = ''
email = ''
balance = 0
account_number = 0

def open_account():
    #declare global variables
    global name
    global telephone
    global email
    global balance
    global account_number

    user_name = input("Enter your name : ")
    user_phone = input("Enter your phone number : ")
    user_mail = input("Enter email address please : ")

    try:
        deposit = float(input("Amount to deposit : "))
    except ValueError:
        print("Unknown value. Please try again ")

    name = user_name
    telephone = user_phone
    email = user_mail
    balance = deposit
    account_number = 1234567890

def transfer_fund():
    print("transfer_fund")

def check_bal():
    global balance
    open_account()
    print("Your account balance is  : {0}".format(balance))


def withdraw():
    print("withdraw")

#open_account()
check_bal()
print("Your details are name : {0} email : {1} phone {2} deposit {3}, thank you for banking with us : ".format(name, email, telephone, balance ))
