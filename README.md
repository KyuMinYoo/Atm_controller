# Atm_controller

The purpose of this project is to implement a simple ATM.

# Installation

clone this repositoy

git clone https://github.com/KyuMinYoo/Atm_controller.git

And then, type this into the terminal to get into the correct directory.

cd Atm_controller

Make sure to be in the correct directory while running this program. 

# The components

1. testfile.txt: original pin/account/balance information text file that is manually edited by users for testing.
   
2. file_copy.py: It creates a duplicate of the test file for other files to interact and change balance.
   The purpose of creating a duplicate file is to maintain the original pin/account/balance information without any changes
   so that we can see when all the changes made in the balance. The name of the duplicate is testfile_copy.txt.
   
4. bank.py: Main bank file that interacts with and modifies testfile_copy.txt.
   It is used to match account for a given pin, see balance, update balance after withdraw/deposit.
   
5. Atm_controller.py: The main interface file that uses bank file for this program.

# How to use

1. Change the testfile.txt manually to test this program. You can add more or delete lines in the file.
   The dictionary format of each lines must stay the same. Also, each pin numbers and account numbers are unique for each line,
   which means that there must not be same pin numbers and account numbers for different lines.
   
   Or You can just use the given testfile.txt without any modifications.

2. Run file_copy.py to create a copy of testfile. File named testfile_copy.txt. is created.

3. Run Atm_controller.py. Follow the instructions shown in the command prompt and enter appropriate numbers for each case
   and for the task in each case.

4. Check testfile_copy.txt after depositting or withdrawing money from a certain account in Atm_controller.py to see whether
   update is made succcessfully. Also, rerun atm_controller.py and see balance of the same account to check the update. 
