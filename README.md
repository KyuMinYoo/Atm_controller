# Atm_controller

The components:

1. testfile.txt: original test file that is manually edited by users for testing.
   
2. file_copy.py: It creates a duplicate of the test file for other files to interact and change balance.
   The name of the duplicate is testfile_copy.txt.
   
3. bank.py: Main bank file that interacts with and modifies testfile_copy.txt.
   It is used to match account for a given pin, see balance, update balance after withdraw/deposit.
   
4. Atm_controller.py: The main interface file that uses bank file for this program.

How to use:

1. Change the testfile.txt manually to test this program. You can add more or delete lines in the file.
   The dictionary format of each lines must stay the same. Also, each pin numbers and account numbers are unique for each line,
   which means that there must not be same pin numbers and account numbers for different lines.
   
   Or You can just use the given testfile.py without any modifications.

2. Run file_copy.py to create a copy of testfile. File named testfile_copy.txt. is created.

3. Run Atm_controller.py. Follow the instructions shown in the command prompt and enter appropriate numbers for each case
   and for the task in each case.

4. Check testfile_copy.txt after withdrawing or depositting money in a certain account in Atm_controller.py to see whether
   update is made succcessfully. Also, rerun atm_controller.py and see balance of the same account to check the update. 
