import datetime as dt
from datetime import datetime
import logging

# menu function
#login menu
def login():
    while True:
        print("\nLogin Menu")
        print("--------------------\n")
        name = str(input("Name: "))
        password = str(input("Password: "))
        if checkDetails(name,password) is True: #checking is user data exists in the user data filee
            print("login successful!")
            writeNameIntoFile("Log of Activities.txt",name)
            writeNameIntoFile("Time Usage.txt",name)
            if name =="David": #Menu for David to view the time usage and log of activities 
                secretMenu()
            else:
                normalMenu()
        else:
            print ("wrong username or password")


#let user login
def checkDetails(name,password):  #to check if the user exist in user data file and the password is correct
    with open("User Data.txt",'r') as fhandler:
        for line in fhandler.readlines():
            us,pw = line.strip().split(",")  #split the data into two data which is user name and password
            
            if (name == us) and (password == pw):
                return True
        else:
            return False        

#David menu
def secretMenu():
    while True:
        print("\nAvailable options:\n")
        print("1- Create new account")
        print("2- Main Menu")
        print("3- view Time Usage")
        print("4- View Log of Activities\n")
        userChoice = enterChoice()
        if userChoice == "1":
            signUp()
        elif userChoice == "2":
            mainMenu()
        elif userChoice == "3":
            viewDetails("Time Usage.txt")
        elif userChoice == "4":
            viewDetails("Log of Activities.txt")
        else:
            print("Wrong options!")
        

def normalMenu():
    while True:
        print("\nAvailable options:\n")
        print("1- Create new account")
        print("2- Main Menu")
        userChoice = enterChoice()
        if userChoice == "1":
            signUp()
        elif userChoice == "2":
            mainMenu()
        else:
            print("Wrong options!")

# Function used in the login menu. let people sign up to become a user
def signUp(): 
    masterList = []
    list = []
    print()
    userName = str(input("Name: "))
    password = str(input("Password: "))
    if validLoginData(userName,password) is True: #to make sure no repeated user name in user data file
        list.append(userName)
        list.append(password)
        masterList.append(list)
        writeDataIntoFile("User Data.txt",masterList, ",") #write and save user name and password in user data file
        print("Registration successfully")
    else:
        print("Please try again")
        signUp()
#main menu for user to selecet option
def mainMenu():
    st=dt.datetime.now()
    while True:
        print("\nTENANT MANAGEMENT")
        print("--------------------\n")
        print("Available Options:\n")
        print("1 - View Data")
        print("2 - Search Data")
        print("3 - Add Data")
        print("4 - Modify Data")
        print("5 - Delete Data")
        print("R - Return to Login Page")
        print("E - Exit\n")
    
        userChoice = enterChoice()
        if userChoice == "1":
            viewDataMenu()
        elif userChoice == "2":
            searchDataMenu()
        elif userChoice == "3":
            addDataMenu()
        elif userChoice == "4":
            modifyDataMenu()
        elif userChoice == "5":
            deleteDataMenu()
        elif userChoice == "R":
            et=dt.datetime.now()
            timeUsage(st,et)
            login()
        elif userChoice == "E":
            et=dt.datetime.now()
            timeUsage(st,et)
            exit()
        else:
            print("Wrong options")

# View Data Menu. Let user to view the complete details
def viewDataMenu():
    while True:
        print("\nVIEW DATA")
        print("--------------------\n")
        print("Available Options:\m")
        print("1 - View Tenant Details")
        print("2 - View Apartment Details")
        print("3 - View Past Tenant Details in Apartment")
        print("E - Back to Main Menu\n")
        userChoice = enterChoice()
        if userChoice == "1":
            viewDetails("Tenant Details.txt")
            logActivities("Viewing Tenanat Details")
        elif userChoice == "2":
            viewDetails("Apartment Details.txt")
            logActivities("Viewing Apartment Details")
        elif userChoice == "3":
            viewDetails("Past Tenant Details.txt")
            logActivities("Viewing Past Tenant Details")  
        elif userChoice == "E":
            mainMenu()
        else:
            print("Oops... Wrong option. Please try again")
            addDataMenu()
#Function used in the view data menu. View all the record in the file
def viewDetails(file):
    with open(file, 'r') as fhandler:
        for record in fhandler:
            print(record.rstrip()) #remove \n

# Search Data Menu. Let user search details based on id or other data
def searchDataMenu():
    while True:
        print("\nSEARCH DATA")
        print("--------------------\n")
        print("Available Options:\n")
        print("1 - Search Tenant Details")
        print("2 - Search Apartment Details")
        print("3 - Search Past Tenant Details Related to Apartment")
        print("E - Back to Main Menu\n")
        userChoice = enterChoice()
        print()
        if userChoice == "1":
            searchDetails("Tenant Details.txt")
            logActivities("Searching Tenanat Details")
        elif userChoice == "2":
            searchDetails("Apartment Details.txt")
            logActivities("Searching Apartment Details")
        elif userChoice == "3":
            searchPastDetails("Past Tenant Details.txt")  # Users can see details of past tenants in an apartment
            logActivities("Searching Tenanat Details")
        elif userChoice == "E":
            mainMenu()
        else:
            print("Oops... Wrong option. Please try again")
            mainMenu()
# Function used in the search data menu. User can search record based on keyword
def searchDetails(file):
    keyword = []
    returnList=[]
    try:
        numbersOfrecords = int(
            input("Enter total keyword you want to search: "))  # to let user enter total data he want to find and this input must be integer
    except ValueError:
        print("\n","Please enter a number!!! ")
        searchDataMenu()
    except:
        print("Please enter correct options !!!")
        searchDataMenu()

    for i in range(0, numbersOfrecords): #let user enter the keyword he want to search
        searchWord = input("Enter anything you want to search: ")
        keyword.append(searchWord)
    print()
    with open(file, 'r') as file:
        for line in file:
            line=line.rstrip()
            for i in keyword: #Loop through the keyword to find a keyword that matches the data in the file
                if i in line:
                    returnList.append(line)

    
    if returnList:
        for i in returnList:
            print(i)
    else:
        print("Record doesn't exists")
#function only for past tenant details. let user can search past tenant rented the apartment
def searchPastDetails(file):
    returnList=[]
    list=[]
    id = input("Enter Apartment id you want to find the past tenant details: ")
    
    with open(file,'r') as file:
        for line in file:
            line=line.rstrip()
            if id in line:
                list.append(line)

    if list:
        for i in list:
            i=i.split(" : ") #split the data into apartment id and tenant id
            with open("Tenant Details.txt",'r') as file: #search the tenant id that related to the apartment id
                for line in file:
                    line=line.rstrip()
                    if i[1] in line:
                        returnList.append(line)
    print(id+":")     
    if returnList:
        for i in returnList:
            print(i)
    else:
        print("Nothing found")
# add Data Menu. Let user add data into file

def addDataMenu():
    while True:
        print("\nADD DATA")
        print("--------------------\n")
        print("Available Options:\n")
        print("1 - Add Tenant Details")
        print("2 - Add Apartment Details")
        print("3 - Add Past Tenant Details Related to Apartment")
        print("E - Back to Main Menu\n")
        userChoice = enterChoice()
        if userChoice == "1":
            addTenantDetails()
            logActivities("Adding Tenanat Details")
        elif userChoice == "2":
            addApartmentDetails()
            logActivities("Adding Apartment Details")
        elif userChoice == "3":
            addRelatedDetails()
            logActivities("Adding Past Tenant Details")
        elif userChoice == "E":
            mainMenu()
        else:
            print("Oops... Wrong option. Please try again")
            addDataMenu()
# add tenant detials function. Let user to enter tenant details such as tenant id, name, ic ,gender place of birth,city of birth,salary, phone number,current employer and work history
def addTenantDetails():
    masterList = []
    list = []

    tenantID = input("Enter tenant's ID (T004): ").upper()
    name = input("Enter tenant's name (Tan Xiao Ming): ").title()
    ic = input("Enter tenant's IC (011111-02-5302): ")
    gender = input("Enter tenant's gender (Male/Female): ").title()
    age = input("Enter tenant's age (17): ")
    pob = input("Enter tenant's place of birth (Penang): ")
    cob = input("Enter tenant's city of birth (Butterworth): ")
    phoneNumber = input("Enter tenant's handphone number (012-4737295): ")
    salary = input("Enter tenant's salary: (RM 300) ")
    currentEmployer = input("Enter tenant's cuerrent employer (Abu): ").title()
    workHistory = input("Enter tenant's workhistory: ")
    print()
    list.append(tenantID)
    list.append(name)
    list.append(ic)
    list.append(gender)
    list.append(age)
    list.append(pob)
    list.append(cob)
    list.append(phoneNumber)
    list.append(salary)
    list.append(currentEmployer)
    # print one to continue enter, or terminate the program
    list.append(workHistory)
    if validTenantData(list) is True: #valid the each data
        masterList.append(list)
        writeDataIntoFile("Tenant Details.txt", masterList,",")
        print("Tenant's (", tenantID, ") record was saved")
    else:
        print("Please try again")
        addDataMenu()
# add apartment detials. Let user to enter apartment details such as id, number, date of acquisition, square footage, expected rent and rental history
def addApartmentDetails():
    masterList = []
    list = []

    apartmentID = str(input("Enter apartment's ID (Example: A001): ")).upper()
    number = str(input("Enter apartment's number (Example: 123): "))
    doa = str(input("Enter apartment's date of acquisition (Example: dd-mm-yyyy): "))
    squareFootage = str(
        input("Enter apartment's squarefootage (Example: 500): "))
    expectedRent = str(
        input("Enter apartment's expected rent (Example: RM 2000): ")).upper()
    rentalHistory = str(input(
        "Enter apartment's rental history (Example: 2016:RM 1000 | 2017:RM 2000 |...):  "))
    list.append(apartmentID)
    list.append(number)
    list.append(doa)
    list.append(squareFootage)
    list.append(expectedRent)
    list.append(rentalHistory)
    if validApartmentData(list) is True: #valid each data
        masterList.append(list)
        writeDataIntoFile("Apartment Details.txt", masterList,",")
        print("Apartment's (", apartmentID, ") record was saved")
    else:
        print("Please enter correct format")
        addDataMenu() 
#add tenat data related to apartment details. Let user enter who has rented the apartment
def addRelatedDetails():
    masterList=[]
    list=[]
    
    apartmentID=str(input("Apartment ID: ")).upper()
    tenantID=str(input("Tenant ID: ")).upper()

    list.append(apartmentID)
    list.append(tenantID)
    if validRelatedData(list) is True:
        masterList.append(list)
        writeDataIntoFile("Past Tenant Details.txt",masterList," : ")
        print("Record was saved")
    else:
        print("Please try again")
        addDataMenu()

# Modify Data Menu. User can modify incorrect data
def modifyDataMenu():
    while True:
        print("\nMODIFY DATA")
        print("--------------------\n")
        print("Available Options:\n")
        print("1 - Modify Tenant Details")
        print("2 - Modify Apartment Details")
        print("E - Back to Main Menu\n")
        userChoice = enterChoice()
        if userChoice == "1":
            modifyData("Tenant Details.txt", "tenant's")
            logActivities("Modifying Tenanat Details")
        elif userChoice == "2":
            modifyData("Apartment Details.txt","apartment's")
            logActivities("Modifying Apartment Details")
        elif userChoice == "E":
            mainMenu()
        else:
            print("Oops... Wrong option. Please try again")

#modify data function. to let user change the incorrect data
def modifyData(file,object):
    id=input("Enter "+object+" id: ").upper() #search record the user want to change
    try:
        filedata=""
        with open(file,"r") as f:
            for line in f:
                if id in line:
                    print(line)
                    oldData=str(input("Enter original data you want to replace: ")).title()
                    newData=str(input("Enter new data you want to replace: ")).title()
                    line=line.replace(oldData,newData)
                    print("Successfully modify")
                filedata += line
            with open(file,"w") as f:
                f.write(filedata)
            
    except IOError:
        print("No data found")
    except:
        print("Please restart program")

# Delete Data Menu. User can delete unwanted data
def deleteDataMenu():
    while True:
        print("\nDELETE DATA")
        print("--------------------\n")
        print("Available Options:\n")
        print("1 - Delete Tenant Details")
        print("2 - Delete Apartment Details")
        print("3 - Delete Past Tenant Details Related to Apartment")
        print("E - Back to Main Menu\n")
        userChoice = enterChoice()
        if userChoice == "1":
            deleteData("Tenant Details.txt")
            logActivities("Deleting Tenanat Details")
        elif userChoice == "2":
            deleteData("Apartment Details.txt")
            logActivities("Deleting Apartment Details")
        elif userChoice == "3":
            deleteData("Past Tenant Details.txt")
            logActivities("Deleting Past Tenant Details")
        elif userChoice == "E":
            mainMenu()
        else:
            print("Oops... Wrong option. Please try again")
#delete data. Delete unwanted record
def deleteData(fileName):
    deletedID=(input("Enter ID you want to delete: ")).upper()

    with open (fileName,"r") as f:
        lines=f.readlines()
    with open(fileName,'w') as writeFile:
        for line in lines:
            if deletedID in line:
                pass
            else:
                writeFile.write(line) #copy and write it down again
    print("Succesfully deleted")

# common functions in many menu
# enter choice and validate the choice
def enterChoice():
    while True:
        try:  # using exceptions for validation
            userChoice = input("Choose An Option: ")
            return userChoice
        except ValueError:
            print("\nInvalid options")  # Error message
            mainMenu()
        except:
            return ("Oops... Something happens")

# write and keep data into file.
def writeDataIntoFile(file, masterList,symbol):
    with open(file, 'a') as fhandler:
        for record in masterList:
            fhandler.write(symbol.join(record)+'\n')

#save user activities in log of activities file
def logActivities(activity):
    logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s',filename="Log of Activities.txt",encoding="utf-8")
    logging.info(activity)

#record the time usage user spend
def timeUsage(startTime,endTime):
    duration=endTime-startTime
    masterList=[]
    list=[]
    list.append(str(startTime))
    list.append(str( endTime))
    list.append(str(duration))
    masterList.append(list)
    writeDataIntoFile("Time Usage.txt",masterList," ,")
       
def writeNameIntoFile(file,input):
    with open(file,"a") as fhandler:
        fhandler.write(input+'\n')
   
# input validation function
# 1. input should only be number
def checkIfInputisInteger(input):
    if input.isdigit():
        return True
    else:
        return False  # This input can only be number

# 2. input should only be word:
def InputCannotContainNumber(input):
    for i in input:
        if i.isdigit():
            return False
    else:
        return True

# 3. check certain place must be number
def checkNumberInString(input, start, end):
    if input[start:end].isdigit():
        return True
    else:
        return False

# 4. The length of the string should be a certain length
def checkConstantLength(input, length):
    if len(str(input)) == length:
        return True
    else:
        return False  # The length of input should be

# 5. the input cannot be empty
def checkEmptyLength(input):
    if len(str(input)) < 1:
        return False  # The value cannot be null
    else:
        return True

# 6. check if input is the only input in the file
def checkUniqueID(file, input):
    listOfList=[]
    with open(file, "r") as file:
        contents = file.read().split("\n")
        for record in contents:
            spl=record.split(",")
            listOfList.append(spl)
        for i in listOfList:
            if input == i[0]:
                return False
        else:
            return True

# 7 check If Input Is in a Date format
def checkDate(input):
    try:
        date = datetime.strptime(input, "%d-%m-%Y")
        return True
    except ValueError:
        return False

# 8 check If Input must Contain Specific character
def checkSpecificCharacter(input, specificWord, position):
    try:
        if specificWord in input[int(position)]:
            return True
        else:
            return False
    except IndexError:
        return False
    except:
        return False

# 9 integer cannot be zero
def checkZerovalue(input):
    try:
        if int(input) == 0:
            return False
        else:
            return True
    except ValueError:
        return "cannot be a string"
    except:
        return "cannot be a string"

#10 def check password length
def checkMinimumLength(input):
    if len(str(input)) < 8:
        return False
    else: 
        return True

#11 some character of the input must be upper
def uppercaseValidation(input):
    for i in input:
        if i.isupper():
            return True
    return False

#12 some character of the input must be lower
def lowercaseValidation(input):
    for i in input:
        if i.islower():
            return True
    return False


# add data input validation
# register  validation
def userNameValidation(input):
    returnValues=[]
    if checkEmptyLength(input) is False:
        returnValues.append("User Name cannot be empty")
    if checkUniqueID("User Data.txt",input) is False:
        returnValues.append("This user name already exists")
    
    if returnValues:
        return{"User Name": returnValues}
    else:
        return True

def passwordValidation(input):
    returnValues=[]
    if InputCannotContainNumber(input) is True:
        returnValues.append("Password shouold contain number")
    if checkMinimumLength(input) is False:
        returnValues.append("Password should at least 8 character")
    if uppercaseValidation(input) is False:
        returnValues.append("Password should contain at least one uppercase character")
    if lowercaseValidation(input) is False:
        returnValues.append("Password should contain at least one lowercase character")
    
    if returnValues:
        return{"Password":returnValues}
    else:
        return True

def validLoginData(name,password):
    masterReturnValue=[]
    if not userNameValidation(name) is True:
        masterReturnValue.append(userNameValidation(name))
    if not passwordValidation(password) is True:
        masterReturnValue.append(passwordValidation(password))
    
    if masterReturnValue:
        for i in masterReturnValue:
            print(i)
    else:
        return True

# tenant validation
# id validation
def tenantIDValidation(input):
    returnValues = []
    # start with t
    if checkSpecificCharacter(input, "T", 0) is False:
        returnValues.append("The tenant's ID should start with T")
    # unique ID
    if checkUniqueID("Tenant Details.txt", input) is False:
        returnValues.append("The tenant's ID is already exists")
    # length of 4
    if checkConstantLength(input, 4) is False:
        returnValues.append("Tenant's ID shoud contain exactly 4 character")
    # last three number must be number
    if checkNumberInString(input, 1, 3) is False:
        returnValues.append("Last three character must be number")

    if returnValues:
        return {"Tenant's ID": returnValues}
    else:
        return True

# name validation
def nameValidation(input):
    returnValues = []
    # cannot contain any number
    if InputCannotContainNumber(input) is False:
        returnValues.append("Name could not contain any number")
    # cannot be empty
    if checkEmptyLength(input) is False:
        returnValues.append("Name cannot be empty")

    if returnValues:
        return {"Name": returnValues}
    else:
        return True

# ic validation
def icValidation(input):
    returnValues = []
    # length of 14
    if checkConstantLength(input, 14) is False:
        returnValues.append("The lenght of IC should be 14 (including -)")
    # contain - in 7 and 10
    if checkSpecificCharacter(input, "-", 6) is False or checkSpecificCharacter(input, "-", 9) is False:
        returnValues.append("Your IC should contain - at position 7 and 10")
    # other must be digit
    if checkNumberInString(input, 0, 5) is False or checkNumberInString(input, 7, 8) is False or checkNumberInString(input, 10, 13) is False:
        returnValues.append("Make sure your enter your real IC number")

    if returnValues:
        return {"IC": returnValues}
    else:
        return True

# gender validation
def genderValidation(input):
    returnValues = []
    # male or female only
    list = ["Male", "Female"]
    if input not in list:
        returnValues.append("Male or Female only")
    if checkEmptyLength(input) is False:
        returnValues.append("Gender could not be empty")

    if returnValues:
        return {"Gender": returnValues}
    else:
        return True

# age validation
def ageValidation(input):
    returnValues = []
    # must be digit
    if checkIfInputisInteger(input) is False:
        returnValues.append("Age should only be integer")
    # cannot empty
    if checkEmptyLength(input) is False:
        returnValues.append("Age cannot be empty")

    if returnValues:
        return {"Age": returnValues}
    else:
        return True

# pob validation
def pobValidation(input):
    returnValues = []
    # cannot be empty
    if checkEmptyLength(input) is False:
        returnValues.append("Place of birth cannot be empty")

    if returnValues:
        return {"Place of birth": returnValues}
    else:
        return True

# cob validation
def cobValidation(input):
    returnValues = []
    # cannot be empty
    if checkEmptyLength(input) is False:
        returnValues.append("City of birth cannot be empty")

    if returnValues:
        return {"City of birth": returnValues}
    else:
        return True

# phone number
def phoneValidation(input):
    returnValues = []
    # length of 10
    if checkConstantLength(input, 11) is False:
        returnValues.append(
            "The lenght of phone number should be 11 (including -)")
    # contain - in 4
    if checkSpecificCharacter(input, "-", 3) is False:
        returnValues.append("Your phone number should contain - at position 4")
    # other must be digit
    if checkNumberInString(input, 0, 2) is False or checkNumberInString(input, 4, 11) is False:
        returnValues.append("Make sure your enter your real phone number")

    if returnValues:
        return {"Phone number": returnValues}
    else:
        return True

# monthly salary validation
def monthlySalaryValidation(input):
    returnValues = []
    # contain RM
    if checkSpecificCharacter(input, "R", 0) is False or checkSpecificCharacter(input, "M", 1) is False:
        returnValues.append("Please add RM before your salary")
    # in position 3 till the end of position must be digit
    if checkNumberInString(input, 4, 15) is False:
        returnValues.append("The other character should be digit")

    if returnValues:
        return {"Monthly salary": returnValues}
    else:
        return True

# current employer validation
def currentEmployerValidation(input):
    returnValues = []
    # cannot be empty
    if checkEmptyLength(input) is False:
        returnValues.append("Employer cannot be empty")

    if returnValues:
        return {"Current employer": returnValues}
    else:
        return True

##Check all of the input. If they are wrong, print them out one by one
def validTenantData(record):
    masterReturnValue = []
    if not tenantIDValidation(record[0]) is True:
        masterReturnValue.append(tenantIDValidation(record[0]))

    if not nameValidation(record[1]) is True:
        masterReturnValue.append(nameValidation(record[1]))

    if not icValidation(record[2]) is True:
        masterReturnValue.append(icValidation(record[2]))

    if not genderValidation(record[3]) is True:
        masterReturnValue.append(genderValidation(record[3]))

    if not ageValidation(record[4]) is True:
        masterReturnValue.append(ageValidation(record[4]))

    if not pobValidation(record[5]) is True:
        masterReturnValue.append(pobValidation(record[5]))

    if not cobValidation(record[6]) is True:
        masterReturnValue.append(cobValidation(record[6]))

    if not phoneValidation(record[7]) is True:
        masterReturnValue.append(phoneValidation(record[7]))

    if not monthlySalaryValidation(record[8]) is True:
        masterReturnValue.append(monthlySalaryValidation(record[8]))

    if not currentEmployerValidation(record[9]) is True:
        masterReturnValue.append(currentEmployerValidation(record[9]))

    if masterReturnValue:
        for i in masterReturnValue:
            print(i)
    else:
        return True

# aprtment's input Validation
# apartment id validation
def apartmentIDValidation(input):
    returnValues = []
    # cannot check all the things in one time
    if checkSpecificCharacter(input, "A", 0) is False:
        returnValues.append("The ID should start with A")
    if checkUniqueID("Apartment Details.txt", input) is False:
        returnValues.append("This aparment ID has already been used")
    if checkConstantLength(input, 4) is False:
        returnValues.append(
            "Apartment's ID format shoud contain four character : A000 ")
    if checkNumberInString(input, 1, 3) is False:
        returnValues.append("Last three character must be number")

    if returnValues:
        return {"ID": returnValues}
    else:
        return True

# number validation
def numberValidation(input):
    returnValues = []
    if checkIfInputisInteger(input) is False:
        returnValues.append("Aparment's number should only contain number")
    if checkConstantLength(input, 3) is False:
        returnValues.append(
            "Aparment's value should contain exactly three number")

    if returnValues:
        return {"Number": returnValues}
    else:
        return True

# doa validation
def doaValidation(input):
    returnValues = []
    if checkEmptyLength(input) is False:
        returnValues.append("The date of acquisition cannot be empty")
    if checkDate(input) is False:
        returnValues.append("The date of acquisition  format is dd-mm-yy")

    if returnValues:
        return {"Date of acquisition": returnValues}
    else:
        return True

# square footage validation
def squareFootageValidtion(input):
    returnValues = []
    if checkIfInputisInteger(input) is False:
        returnValues.append("The square footage should only be number")
    if checkZerovalue(input) is False:
        returnValues.append("The value cannot be zero")
    if checkEmptyLength(input) is False:
        returnValues.append("The sqaure footage cannot be empty")

    if returnValues:
        return {"Sqaure footage": returnValues}
    else:
        return True

# ecpected rent validation
def expectedRentValidation(input):
    returnValues = []
    # this need to check again
    if checkSpecificCharacter(input, "R", 0) is False or checkSpecificCharacter(input, "M", 1) is False:
        returnValues.append("Add RM before expected rent")  # This got problems
    if checkNumberInString(input, 4, 15) is False:
        returnValues.append("The expected rent should contain number")
    if checkEmptyLength(input) is False:
        returnValues.append("The expected rent cannot be empty")

    if returnValues:
        return {"Expected rent": returnValues}
    else:
        return True


# #Check all of the input. If they are wrong, print them out one by one
def validApartmentData(record):
    masterReturnValue = []
    if not apartmentIDValidation(record[0]) is True:
        masterReturnValue.append(apartmentIDValidation(record[0]))

    if not numberValidation(record[1]) is True:
        masterReturnValue.append(numberValidation(record[1]))

    if not doaValidation(record[2]) is True:
        masterReturnValue.append(doaValidation(record[2]))

    if not squareFootageValidtion(record[3]) is True:
        masterReturnValue.append(squareFootageValidtion(record[3]))

    if not expectedRentValidation(record[4]) is True:
        masterReturnValue.append(expectedRentValidation(record[4]))

    if masterReturnValue:
        for i in masterReturnValue:
            print(i)
    else:
        return True

#past tenant details validation
#apartment ID validation
def RelatedApartmentID(input):
    returnValues=[]
    if checkUniqueID("Apartment Details.txt",input) is True:
        returnValues.append("Apartment id didn't exits in apartment details")
    if checkSpecificCharacter(input, "A", 0) is False:
        returnValues.append("Apartment ID should start with A")
    if checkConstantLength(input, 4) is False:
        returnValues.append(
            "Apartment's ID format shoud contain four character : A000 ")
    if checkNumberInString(input, 1, 3) is False:
        returnValues.append("Last three character must be number")
    
    if returnValues:
        return{"Apartment ID": returnValues}
    else:
        return True

#tenant id validation
def RelatedTenantID(input):
    returnValues=[]
    if checkUniqueID("Tenant Details.txt",input) is True:
        returnValues.append("Tenant id didn't exits in tenant details")
    if checkSpecificCharacter(input, "T", 0) is False:
        returnValues.append("The tenant's ID should start with T")
    # length of 4
    if checkConstantLength(input, 4) is False:
        returnValues.append("Tenant's ID shoud contain exactly 4 character")
    # last three number must be number
    if checkNumberInString(input, 1, 3) is False:
        returnValues.append("Last three character must be number")
    
    if returnValues:
        return{"Tenant ID": returnValues}
    else:
        return True

#apartment and tenant id validation
def RelatedData(input1,input2):
    string=(input1+" : "+input2)
    returnValues=[]
    if checkUniqueID("Past Tenant Details.txt",string) is False:
        returnValues.append( "Same data exists in Past Tenant Details File")

    if returnValues:
        return{"Related Data":returnValues}
    else:
        return True

#Check all of the input. If they are wrong, print them out one by one
def validRelatedData(record):
    masterReturnValues=[]
    if not RelatedApartmentID(record[0]) is True:
        masterReturnValues.append(RelatedApartmentID(record[0]))

    if not RelatedTenantID(record[1]) is True:
        masterReturnValues.append(RelatedTenantID(record[1]))
    
    if not RelatedData(record[0],record[1]) is True:
        masterReturnValues.append(RelatedData(record[0],record[1]))
    

    if masterReturnValues:
        for i in masterReturnValues:
            print(i)
    else:
        return True

login()
