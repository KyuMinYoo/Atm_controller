import ast
import numpy as np

#Checks the validity of the pin number entered by a user, and then returns the account that matches that number
def pin_number_checker(pin):

    index=-1   
    with open("testfile_copy.txt", "r") as file:
        for line in file:
            line=ast.literal_eval(line)
            if line['pin']==pin:
                line=str(line)
                index=line.strip()

    if(index==-1):
        return index
    else:
        index=ast.literal_eval(index)
        index=index["account"]
        return index

#Searches and returns the current balance that matches the given account number 
def check_balance(account_number):
  
    with open("testfile_copy.txt", "r") as file:
        for line in file:
            line=ast.literal_eval(line)
            if line['account']==account_number:
                line=str(line)
                index=line.strip()
   
    index=ast.literal_eval(index)
    index=index["balance"]

    return index
    
#Method for withdrawing/depositting money. This method updates the balance that matches the given account number by the amount that has been withdrawn/deposited.
def update_balance(account_number, value):  
    
    temp=[]
    with open("testfile_copy.txt", "r") as file:
        for line in file:
            line=ast.literal_eval(line)
            temp.append(line)
            if line['account']==account_number:
                line=str(line)
                index=line.strip()
   
    index=ast.literal_eval(index)

    balance=index["balance"]

    for i in range (len(temp)):
        if(temp[i]['balance']==balance):
            temp[i]['balance']=balance+value

    with open("testfile_copy.txt", "w") as file:
        for i in range(len(temp)):
            line=temp[i]
            line=str(line)
            if(i<len(temp)-1):
                file.write(line+"\n")
            else:
                file.write(line)

    return balance+value



