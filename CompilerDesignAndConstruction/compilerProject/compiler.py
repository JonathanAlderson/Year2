import random,language,sys,time,language,numbers,string,os
from lexer import Lexer
from myParser import Parser


#################################
#################################
#################################

#######     COMPILER SETTINGS ###
doPrintoutCode = False
doPrintoutAssertions = False
doPrintoutGlobalClassTable = False
doPrintoutGlobalMethodTable = False
exitOnErrors = False

# GENERAL FUNCTIONS
# contains a few functions that are used multiple times
# in the lexer and the parser
#####################################################################
def displayMessage(message,isError=False):
    """ Produces nicely formatted messages for either messages or errors """
    print("---------------------\n",message,"\n---------------------")
    if(isError):
        if(exitOnErrors):
            sys.exit()
        else:
            print("\nWARNING")
            time.sleep(1)

def error(token,message=""):
    # displays a message to the user
    displayMessage("Syntax Error On Line " + str(token[2]) + "\n At Or Near '" + token[0] + "'" + "\n" +" "+ message ,True)

def getCommandLineArguments():
    """ This function will look to see if the user
        has ran the program with a filename, if they
        have, the program will attempt to read the file"""
    if(len(sys.argv) == 1):
        return "None"
    return (sys.argv[1])

def getFilesInDirectory(directory):
    """ Returns a list of all files in directory, not including sub directories"""
    jackFiles = []
    for files in os.walk(directory):
        for file in files[2]:
            if '.jack' in file:
                jackFiles.append(files[0] + file)
    # case where the user just wants to compile a single file
    # and not a directory
    if(len(jackFiles) == 0):
        return [directory]
    return jackFiles

def printoutTables():
    """ Used for debugging, can be turned on or off in settings """
    if(doPrintoutCode):
        print("\n\nGenerated Code\n\n")
        for program in vmCode:
            if(program not in ["Array","Keyboard","Math","Memory","Output","Screen","String","Sys"]):
                lineNumber = 1
                print("\n" + program + "\n" + "--------------" + "\n")
                for line in vmCode[program]:
                    print(str(lineNumber).ljust(5," "),end="")
                    print(" ".join(str(i) for i in line))
                    lineNumber += 1

    if(doPrintoutGlobalClassTable):
        print("Global Class Table\n---------------\n")
        for keys,values in globalClassTable.items():
            if(keys not in ["Array","Keyboard","Math","Memory","Output","Screen","String","Sys"]):
                print("Class: ",keys)
                for value in values:
                    print("   ",value)
    if(doPrintoutGlobalMethodTable):
        print("\n\nGlobal Method Table\n---------------\n")
        for className,values in globalMethodTable.items():
            if(className not in ["Array","Keyboard","Math","Memory","Output","Screen","String","Sys"]):
                print("Class: ",className)
                for funcName in values:
                    print("    Func: ",funcName)
                    for values in globalMethodTable[className][funcName]:
                        print("        ",values)
    if(doPrintoutAssertions):
        print("\n")
        print(str(len(assertions)) + " Assertions to check")
        for assertion in assertions:
           print(assertion)

def findFileFromClassName(className):
    """ given a class name, we give the full directory """
    for thisFile in filesToCompile:
        fileClassName = thisFile.split("/")[-1][:-5]
        if(fileClassName == className):
            return thisFile[:-5]
    error("Invalid File Name")
    sys.exit()
    time.sleep(5)


def saveFiles():
    """ Saves all new .vm files in their respective directories """
    for program in vmCode:
        if(program not in ["Array","Keyboard","Math","Memory","Output","Screen","String","Sys"]):
            print("Now saving: " + str(findFileFromClassName(program)))
            file = open(str(findFileFromClassName(program)) + ".vm","w+")
            for line in vmCode[program]:
                file.write(" ".join(str(i) for i in line) + "\n")
            file.close()


def checkAssertions(assertions,globalClassTable,globalMethodTable,classMethods):
    """ This checks for if variables/methods from classes exist, if functions,
        were called with the correct number of arguments, if the data types are correct,
        and will report errors if any of them are wrong """
    print("Starting Checks")
    for check in assertions:
        found = False
        typeOfCheck = check[0]
        className = check[1]
        lineNumber = check[-1]
        if(typeOfCheck == "exists"):
            if(check[2]): # it is a function
                try:
                    # if the function is in the class' dict
                    if(check[3] in globalMethodTable[className]):
                        found = True
                except KeyError:
                    error([check[1],check[0],lineNumber],"Class does not exist")
            else: # it is just a variable from a class
                # check if the variable name is in all the names from that class
                if(check[3] in list(zip(*globalClassTable[className]))[0]):
                    found = True

            if(found == False):
                error([check[1]+"."+check[3],"",lineNumber],"Function or variable does not exist")

        elif(typeOfCheck == "typeCheck"):
            expected = ""
            actual = ""
            if(check[2]): # it is a function
                for function in classMethods[check[1]]: # look through all the functions from the class
                    if(function[0] == check[3]): # if they have the same name
                        if(function[1] == check[4]): # check they have the same type
                            expected = function[1]
                            actual = check[4]
                            found = True
            else:
                for variable in globalClassTable[className]:
                    if(variable[0] == check[3]): # they have the same name
                        expected = variable[1]
                        actual = check[4]
                        found = True

            if(expected != actual or found == False and actual != ""):
                error([check[1]+"."+check[3],"",lineNumber],"Mismatching types in expression:\n Expected " + str(expected) + " instead got " + str(actual))

        elif(typeOfCheck == "numberOfArguments"):
            for function in classMethods[check[1]]: # look through all the functions from the class
                if(function[0] == check[2]): # if they have the same name
                    if(function[2] != check[3]): # check they have the same number of args
                        error([str(check[1])+"."+str(check[2]),"",lineNumber],"Function takes " + str(function[2]) + " arguments, but you used " + str(check[3]))
        else:
            pass
    print("\n\n" + str(len(assertions))+ " semantic checks passed.")

def fixVMCode(vmCode):
    """Fills in the blanks for number of arguments and number of local variables"""
    for program in vmCode:
        try:
            for line in vmCode[program]:
                if(line[0] == "call"):
                    # look through every function in class until same name found
                    for function in classMethods[line[1].split(".")[0]]:
                        if(line[1].split(".")[1] == function[0]):
                            line[2] += function[2] # assign the correct number of args
                elif(line[0] == "function"):
                    # find the number of local arguments for that function
                    count = 0
                    # look at all vars in all classes. Find how many are not arguments
                    for variable in globalMethodTable[line[1].split(".")[0]][line[1].split(".")[1]]:
                        if(variable[2] != "argument"): #
                            count += 1
                    line[2] = count
        except Exception as e:
            print(e)
            displayMessage("Internal Compiler Error",True)
    return vmCode

###################################################################


# we perfom lexical analysis on each file in the parsing stage
# so even though we do not make a lexical call, it still happends
# just before we start the Parsing
# Now parse each file, one at a time
# we will keep the symbol table for every class here
# and keep the symbol table for each

# making the global symbol tables
globalClassTable = {}
globalMethodTable = {}
assertions = []
classMethods = {}
vmCode = {}




# Get all the files we need to compile
directory = getCommandLineArguments()
filesToCompile = getFilesInDirectory(directory)
osFiles = ['Jack_Programs/jack-os/Array.jack', 'Jack_Programs/jack-os/Keyboard.jack', 'Jack_Programs/jack-os/Math.jack', 'Jack_Programs/jack-os/Memory.jack', 'Jack_Programs/jack-os/Output.jack', 'Jack_Programs/jack-os/Screen.jack', 'Jack_Programs/jack-os/String.jack', 'Jack_Programs/jack-os/Sys.jack']
filesToCompile =  osFiles + filesToCompile
displayMessage("\n\n\nPrograms to Compile")
for file in filesToCompile:
    print(file)
print("\n\n")
time.sleep(0.3)

for file in filesToCompile:
    parser = Parser(file,exitOnErrors)
    symbolTables = parser.parse()

    # update the dictionaries for the symbol tables
    globalClassTable = symbolTables[0]
    globalMethodTable[file.split("/")[-1].split(".")[0]] = symbolTables[1]
    assertions = assertions + symbolTables[2]
    classMethods = symbolTables[3]
    vmCode[file.split("/")[-1].split(".")[0]] = symbolTables[4]

checkAssertions(assertions,globalClassTable,globalMethodTable,classMethods)
vmCode = fixVMCode(vmCode)
printoutTables()
saveFiles()
displayMessage("\n\n\nDone")
