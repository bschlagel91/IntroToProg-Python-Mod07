# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Pickling and Structured error handling
# ChangeLog (Who,When,What):
# Brandon Schlagel, 8.22.21,Pickling binary files and structured error handling
# ---------------------------------------------------------------------------- #
# Create a script that pickles a current binary file and combines the user input
# another file.  Use Structured error proofing to make sure the user has a user friendly
# message with easy to follow instructions
lstcustomer = []
intid = ''
strname = ''
import pickle  # This imports code from another code file!
while True:

    try:
        intId = int(input("Enter an Id: "))
        break
    except:
        print("please input a number, not a letter!\n")

while True:
    try:
        strname = str(input("Enter a Name: "))
        break
    except:
        print("please use a letter or text! \n")
lstcustomer = [intId, strname]
print(lstcustomer)

# Now we store the data with the pickle.dump method
objFile = open("AppData.dat", "ab")
pickle.dump(lstcustomer, objFile)
objFile.close()

# we read the data back with the pickle.load method
objFile = open("AppData.dat", "rb")
objFileData = pickle.load(objFile) #load() only loads one row of data.
print(objFileData)
objFile.close()


