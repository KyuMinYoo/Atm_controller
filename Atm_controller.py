import numpy as np
import ast
from bank import pin_number_checker 
from bank import check_balance
from bank import update_balance

#This atm controller uses methods from bank for user interface

pin_number=input("welcome to the atm. Please enter your 4 digit PIN number.\n")
account=pin_number_checker(int(pin_number))
while(account==-1):
    pin_number=input("Wrong pin or not a valid pin. Please enter your 4 digit PIN number again.\n")
    account=pin_number_checker(int(pin_number))
print("Your account number:")
print(account)

number=input("what would you like to do? \nplease choose one of the following. \n1. See balance \n2. withdraw money \n3. Deposit money\n")
number=int(number)
while not (number==1 or number==2 or number==3):
    number=input("please choose one of the three options\n")
    number=int(number)

if(number==2):
    print("Your current balance:")
    balance=check_balance(account)
    print(balance)
    amount=input("Please enter the amount you would like to withdraw:\n")
    amount=int(amount)*-1
    while(abs(amount)>balance):
        amount=input("You can not withdraw more than your balance. Please enter the amount less than your current balance.\n")
        amount=int(amount)*-1
    new_balance=update_balance(account, amount)
    print("Please take the money and the card.")
    print("Your new balance:")
    print(new_balance)
    print("Thank you very much for using the atm")
    exit()
    
elif(number==3):
    print("Your current balance:")
    balance=check_balance(account)
    print(balance)
    amount=input("Please enter the amount you would like to deposit:\n")
    amount=int(amount)
    new_balance=update_balance(account, amount)
    print("Your new balance:")
    print(new_balance)
    print("Thank you very much for using the atm")
    exit()
    
elif(number==1):
    print("Your current balance:")
    balance=check_balance(account)
    print(balance)
    choice=input("Please choose '1 or 2' for the following options: \n1. withdraw money \n2. Deposit money\nOr Press any other keys to exit\n")
    choice=int(choice)

if not (choice==1 or choice==2):
    print("Thank you very much for using the atm")
    
elif(choice==1):
    amount=input("Please enter the amount you would like to withdraw:\n")
    amount=int(amount)*-1
    while(abs(amount)>balance):
        amount=input("You can not withdraw more than your balance. Please enter the amount less than your current balance.\n")
        amount=int(amount)*-1
    new_balance=update_balance(account, amount)
    print("Please take the money and the card.")
    print("Your new balance:")
    print(new_balance)
    print("Thank you very much for using the atm")
    
elif(choice==2):
    amount=input("Please enter the amount you would like to deposit:\n")
    amount=int(amount)
    new_balance=update_balance(account, amount)
    print("Your new balance:")
    print(new_balance)
    print("Thank you very much for using the atm")
   


