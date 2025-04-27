import shutil

#Makes a copy of the original test file so that the duplicate can be modified by the bank file
shutil.copy('testfile.txt', 'testfile_copy.txt')