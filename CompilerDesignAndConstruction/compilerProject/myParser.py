import language,sys,time
from lexer import Lexer

class Parser:

    rawFile = ""
    lineNumber = 0
    tokensList = []
    lexemeList = []

    printFuncNames = False
    printAcceptence = False
    exitOnErrors = False

    currentClass = "" # while parsing all the files, we need to know the current class
    currentSubroutine = "" # same for the functions

    classSymbolTable = {} # holds the info on all the variables in the class
                          # {[variableName,type,kind,id,initialised]}

    methodSymbolTable = {} # holds all the info on all the variables in each function
                           # {[variableName,type,kind,id,initialised]}

    classMethods = {}  # holds the information about all the functions a class has
                       #  {functionName,returnType,numberOfArguments}

    assertions = []    # used at the end of parsing to check and report errors
                       # ["typeCheck",className,isFunction,funcOrVarName,expectedType,lineNumber]
                       # ["exists",className,isFunction,funcOrVarName,lineNumber]
                       # ["numberOfArguments",className,functionName,expectedNumber,lineNumber]

    unresolvedDeclarations = []

    vmCode = []   # used for generation of the vm code

    hasReturnStatement = False  # used for checking if all code paths return a value

    unreachableCode = False

    fileName = ""

    # things for VM Code Generation
    whileCounter = 0
    whileEndCounter = 0
    ifTrueCounter = 0
    ifFalseCounter = 0
    inVoidFunction = False

    lexer = Lexer()

    def __init__(self,fileName,exitOnErrors):
        self.exitOnErrors = exitOnErrors
        self.lexer.lexicalAnalysis(fileName,self.exitOnErrors)
        self.fileName = fileName

    def displayMessage(self,message,isError=False):
        """ Produces nicely formatted messages for either messages or errors """
        print("---------------------\n",message,"\n---------------------")
        if(isError):
            if(self.exitOnErrors):
                sys.exit()
            else:
                print("WARNING\n")
                time.sleep(1)
    def error(self,token,message=""):
        self.displayMessage("Reporting from " + str(self.fileName) + "\n Error On Line " + str(token[2]) + "\n At Or Near '" + token[0] + "'" + "\n" +" "+ message ,True)

    def acceptToken(self,token):
        if(self.unreachableCode):
            self.error(token,"Unreachable Code")
        if(self.printAcceptence):
            print("Accepted: ",token)

    def findMaxID(self,object,varKind):
        maxID = -1
        for obj in object:
            if(obj[2] == varKind):
                if(obj[3] > maxID):
                    maxID = obj[3]
        return maxID+1 # this is the next ID we should use for the variable

    def checkDeclared(self,nextToken):
        """ This checks weather the token we want to use already exists
            in the symbol table, first as a local variable, then checking global """
        found = False
        thisClassVariables = self.classSymbolTable[self.currentClass]
        thisMethodVariables = self.methodSymbolTable[self.currentSubroutine]
        # see if the variable is a local variable
        for var in thisMethodVariables:
            if(nextToken[0] in var):
                found = True
        # now check to see if it's a global variable
        if(found == False):
            for var in thisClassVariables:
                if(nextToken[0] in var):
                    found = True

        if(found == False):
            # since this function is only checking for local variables,
            # if it is not found here, it will not be in another class
            # so it is an error
            self.error(nextToken,"Variable not declared in local scope or class")

    def checkOnlyUsedOnce(self,nextToken,scope):
        """ This function checks that the identifier is only declared once,
            so in each function there is only one thing with that name,
            in each class there is only one thing with that name,
            and in the program there is only one thing with the same name"""

        if(scope == "class"):
            toSearch = self.classSymbolTable[self.currentClass]
        elif(scope == "subroutine"):
            toSearch = self.methodSymbolTable[self.currentSubroutine]

        count = 0

        for item in toSearch:
            if(nextToken[0] == item[0]):
                count+=1

        if(count != 1):
            self.error(nextToken,str("Variable with same name already declared in this " + str(scope)))

    def checkInitlised(self,nextToken):
        """ This function will check if a variable trying to be used is un initilised,
            this function will be ran after check declared, so we know it must,
            already exist. But we can only check if the variable to initialised
            is local to the function, since it does not make sense to check a global."""
        thisMethodVariables = self.methodSymbolTable[self.currentSubroutine]
        # look through the local variables, and see if it is undeclared
        for var in thisMethodVariables:
            if(nextToken[0] == var[0]):
                # meaning the varaible is uninitalised
                if(var[4] == False):
                    self.error(nextToken,"Variable must be initilised before being used")

    def findVariableType(self,className,methodName,token):
        """ Given the class and subroutine the variable is in, we will return
            what type the variable is. If the variable is from another class,
            we will have to check it at the end, since we do not know if the
            class has been parsed yet."""
        # then we are just looking for a class variable
        for var in self.classSymbolTable[className]:
            if(var[0] == token[0]): # they have the same name

                return var[1] # the type
        for var in self.methodSymbolTable[methodName]:
            if(var[0] == token[0]):
                if(var[1] == "char"):
                    return "int"  # becaues chars are just treated the same as ints
                return var[1]

        # then it is just the class name, so that is the type
        return token[0]

    def getFunctionInfo(self):
        """ find out what the function should be returning """
        for func in self.classMethods[self.currentClass]:
            if(func[0] == self.currentSubroutine):
                if(func[1] == "char"):
                    func[1] = "int"  # todo, we are treating ints as chars
                return(func) # returns the name, return type and num of args
        self.error("Internal compiler error")

    def vmCodeInfo(self,nextToken):
        """ Given a token, this function will find if the var is argument or local, and the value """
        info = []
        newInfo = [] # for a special case calling 'new' function
        for variable in self.methodSymbolTable[self.currentSubroutine]:
            if(variable[0] == nextToken[0]):
                info = [variable[2],variable[3]]
            if(variable[1] == nextToken[0]):
                newInfo = [variable[2],variable[3]]
        if(info == []):
            for variable in self.classSymbolTable[self.currentClass]:
                    if(variable[0] == nextToken[0]):
                        info = [variable[2],variable[3]]
                    if(variable[1] == nextToken[0]):
                        newInfo = [variable[2],variable[3]]
        if(info == []):
            info = newInfo
        if(info[0] == "argument"):
            found = False
            for func in self.classMethods[self.currentClass]:
                if(func[0] == self.currentSubroutine):
                    if(func[3] == "method"):
                        found = True

            if(found == False):
                info[1] -= 1 # no longer count 'this', so -1
        if(info[0] == "var"):
            info[0] = "local" # VM uses 'lcoal' instead of 'var', so must be changed
        if(info[0] == "field"):
            info[0] = "this"
        if(info[1] == -1):
            info[6] = "error" ## there has been an error (handled elsewhere)
        return info

    def classDeclar(self):
        if(self.printFuncNames):
            print("classDeclar")
        nextToken = self.lexer.getNextToken()
        if(nextToken[0] == "class"):
            # do nothing, we are happy
            self.acceptToken(nextToken)
        else:
            self.error(nextToken," Expected start symbol")

        nextToken = self.lexer.getNextToken()
        if(nextToken[1] == "identifier"):
            # do nothing, we are happy
            self.acceptToken(nextToken)
            self.currentClass = nextToken[0] # updates which class we are parsing
            # now we have parsed the class, we will add it to our list
            # we also check if the class is already in the symbol table,
            # if so, we terminate the program
            if(nextToken[0] in self.classSymbolTable):
                self.error(nextToken,"Class with this name already exists")
            else:
                self.classSymbolTable[nextToken[0]] = []
                self.classMethods[nextToken[0]] = []

        else:
            self.error(nextToken," Expected identifier")

        nextToken = self.lexer.getNextToken()
        if(nextToken[0] == "{"):
            # do nothing, we are happy
            self.acceptToken(nextToken)
        else:
            self.error(nextToken," Expected {")

        nextToken = self.lexer.peekNextToken()
        while(nextToken[0] in ["static","field","constructor","function","method"]):
            self.inVoidFunction = False
            if(nextToken[0] in ["static","field"]):
                self.classVarDeclar()
            elif(nextToken[0] in ["constructor","function","method"]):
                self.allPathsReturnValue = False
                self.subroutineDeclar()
                self.allPathsReturnValue = True
                if(self.allPathsReturnValue == False):
                    self.error(nextToken,"All code paths must return value")
            nextToken = self.lexer.peekNextToken()

        nextToken = self.lexer.getNextToken()
        if(nextToken[0] == "}"):
            # do nothing, we are happy
            self.acceptToken(nextToken)
        else:
            self.error(nextToken,"Expected }")

    def memberDeclar(self):
        if(self.printFuncNames):
            print("memberDeclar")
        nextToken = self.lexer.peekNextToken()
        if(nextToken[0] in ["static","field"]):
            self.classVarDeclar()
        elif(nextToken[0] in ["constructor","function","method"]):
            self.subroutineDeclar()
        else:
            self.error(nextToken," Expected static,field,constructor,function,method")

    def classVarDeclar(self):
        # info used later for code gen
        varName = ""
        varType = ""
        varKind = ""
        if(self.printFuncNames):
            print("classVarDeclar")
        nextToken = self.lexer.getNextToken()
        if(nextToken[0] in ["static","field"]):
            varKind = nextToken[0]
            self.acceptToken(nextToken)
        else:
            self.error(nextToken," Expected static field")

        varType = self.lexer.peekNextToken()[0] # we do not need to check this
                                                # as it is checked next
        # then we look for the type
        self.type()

        nextToken = self.lexer.getNextToken()
        if(nextToken[1] == "identifier"):
            self.acceptToken(nextToken)
            varName = nextToken[0]

        else:
            self.error(nextToken," Expected identifier")

        # add the first variable to the symbol table
        varID = self.findMaxID(self.classSymbolTable[self.currentClass],varKind)
        self.classSymbolTable[self.currentClass].append([varName,varType,varKind,varID,True])

        # check we haven't used this variable in this class already
        self.checkOnlyUsedOnce(nextToken,"class")

        nextToken = self.lexer.getNextToken()
        while(nextToken[0] == ","):
            self.acceptToken(nextToken)
            nextToken = self.lexer.getNextToken()
            if(nextToken[1] == "identifier"):
                self.acceptToken(nextToken)
                varName = nextToken[0] # because now we need to add another one

            else:
                self.error(nextToken," Expected identifier")

            # add the next variable to the symbol table
            # the type and kind stay the same
            varID = self.findMaxID(self.classSymbolTable[self.currentClass],varKind)
            self.classSymbolTable[self.currentClass].append([varName,varType,varKind,varID,True])

            # check we haven't used the variable in this class already
            self.checkOnlyUsedOnce(nextToken,"class")

            nextToken = self.lexer.getNextToken()

        if(nextToken[0] == ";"):
            self.acceptToken(nextToken)
        else:
            self.error(nextToken," Expected ;")

    def type(self):
        if(self.printFuncNames):
            print("type")
        nextToken = self.lexer.getNextToken()
        if(nextToken[0] in ["int","char","boolean" ] or nextToken[1] == "identifier"):
            # do nothing, we are happy
            self.acceptToken(nextToken)
        else:
            self.error(nextToken," Expected type")

    def subroutineDeclar(self):
        # these are used to generate the vm code
        # and for the class methods data structure
        subroutineType = ""
        returnType = ""
        numberOfArguments = 0
        functionName = ""
        isConstructor = False
        isMethod = False

        # reset these since they are unique for each subrouine
        # i'm only doing this to match the nand to tetris compiler
        self.whileCounter = 0
        self.whileEndCounter = 0
        self.ifTrueCounter = 0
        self.ifFalseCounter = 0

        if(self.printFuncNames):
            print("subroutineDeclar")
        nextToken = self.lexer.getNextToken()
        if(nextToken[0] in ["constructor","function","method"]):
            # do nothing, we are happy
            self.acceptToken(nextToken)
            subroutineType = nextToken[0]
            if(nextToken[0]  == "constructor"):
                # used later for code generation
                isConstructor = True
            if(nextToken[0] == "method"):
                # used later for code generation
                isMethod = True

        else:
            self.error(nextToken," Expected constructor, function or method")

        nextToken = self.lexer.peekNextToken()
        if(nextToken[0] in ["int","char","boolean","void"] or nextToken[1] == "identifier"):
            # so we know what data type this function call is
            returnType = nextToken[0]
            # do nothing, we are happy
            if(nextToken[0] == "void"):
                nextToken = self.lexer.getNextToken()
                self.inVoidFunction = True
                self.acceptToken(nextToken)
            else:
                self.type()
        else:
            self.error(nextToken," Expected type or identifier (1)")

        nextToken = self.lexer.getNextToken()
        if(nextToken[1] == "identifier"):
            # do nothing, we are happy
            self.acceptToken(nextToken)
            functionName = nextToken[0]
            self.currentSubroutine = functionName # so we know what function we are in
            # sets up a space in the table for this functions variables
            # and checks if it already exitst
            if(nextToken[0] in self.methodSymbolTable):
                if(self.methodSymbolTable[nextToken[0]][0][-1] == self.currentClass):
                    self.error(nextToken,"Subroutine with same name already exists in class")
                else:
                    # then a subroutine with the same name exists, but in a
                    # different class, so it's fine
                    self.methodSymbolTable[nextToken[0]] = []
            else:
                self.methodSymbolTable[nextToken[0]] = []
        else:
            self.error(nextToken," Expected identifier")

        nextToken = self.lexer.getNextToken()
        if(nextToken[0] == "("):
            # do nothing, we are happy
            self.acceptToken(nextToken)
        else:
            self.error(nextToken," Expected (")


        # now we know we are in the function, we add the first argument
        # add the first 'this' argument
        varID = self.findMaxID(self.methodSymbolTable[self.currentSubroutine],"argument")
        self.methodSymbolTable[self.currentSubroutine].append(["this",self.currentClass,"argument",varID,True,self.currentClass])

        # this one can accept void, so we check if it will meet the paramList
        # if not, we will just go on to the next one
        nextToken = self.lexer.peekNextToken()
        if(nextToken[0] in ["int","char","boolean","void"] or nextToken[1] == "identifier"):
            # do nothing, we are happy
            # paramList returns the number of arguments
            numberOfArguments = self.paramList()

        # now we add the generated vm code to our list
        # and add the function info to our class methods
        self.vmCode.append(["function",self.currentClass + "." + functionName,"numberOfLocalVariables"])

        self.classMethods[self.currentClass].append([functionName,returnType,numberOfArguments,subroutineType])

        # code Generation
        if(isConstructor):
            numberOfFieldVariables = 0
            for var in self.classSymbolTable[self.currentClass]:
                if(var[2] == "field"):
                    numberOfFieldVariables += 1
            self.vmCode.append(["push","constant",numberOfFieldVariables])
            self.vmCode.append(["call","Memory.alloc",0]) # correct args will be updated later
            self.vmCode.append(["pop","pointer",0])

        if(isMethod):
            self.vmCode.append(["push","argument",0])
            self.vmCode.append(["pop","pointer",0])

        nextToken = self.lexer.getNextToken()
        if(nextToken[0] == ")"):
            # do nothing, we are happy
            self.acceptToken(nextToken)
        else:
            self.error(nextToken," Expected )")

        nextToken = self.lexer.peekNextToken()
        if(nextToken[0] == "{"):
            # do nothing, we are happy
            self.subRoutineBody()
        else:
            self.error(nextToken," Expected {")

    def paramList(self):
        varName = ""
        varType = ""
        varKind = "argument"
        numberOfArguments = 1

        if(self.printFuncNames):
            print("paramList")
        nextToken = self.lexer.peekNextToken()
        if(nextToken[0] in ["int","char","boolean"] or nextToken[1] == "identifier"):
            self.type()
            varType = nextToken[0]
        else:
            self.error(nextToken," Expected type")

        nextToken = self.lexer.getNextToken()
        if(nextToken[1] == "identifier"):
            # do nothing, we are happy
            self.acceptToken(nextToken)
            varName = nextToken[0]

        else:
            self.error(nextToken," Expected identifier")



        # and now we add the variable to the symbol table
        varID = self.findMaxID(self.methodSymbolTable[self.currentSubroutine],varKind)
        self.methodSymbolTable[self.currentSubroutine].append([varName,varType,varKind,varID,True,self.currentClass])


        # check we haven't used this variable name before
        self.checkOnlyUsedOnce(nextToken,"subroutine")

        # now we check if there is another list entry,
        # we can just recursively call the fcuntion if this is the case
        nextToken = self.lexer.peekNextToken()
        if(nextToken[0] == ","):
            nextToken = self.lexer.getNextToken()
            self.acceptToken(nextToken)
            numberOfArguments += self.paramList()

        # if there is no comma that is fine and we just return
        return numberOfArguments

    def subRoutineBody(self):
        if(self.printFuncNames):
            print("subRoutineBody")
        # this must be set to true by the end of the subroutine,
        # or else not all code paths return a value
        self.hasReturnStatement = False
        nextToken = self.lexer.getNextToken()
        if(nextToken[0] == "{"):
            # do nothing, we are happy
            self.acceptToken(nextToken)
        else:
            self.error(nextToken," Expected {")

        # zero to many case
        nextToken = self.lexer.peekNextToken()
        while(nextToken[0] in ["var","let","if","while","do","return"]):
            # do nothing, we are happy
            if(nextToken[0] == "var"):
                self.varDeclarStatement()
            elif(nextToken[0] == "let"):
                self.letStatement()
            elif(nextToken[0] == "if"):
                if(self.ifStatement()):
                    self.hasReturnStatement = True

            elif(nextToken[0] == "while"):
                self.whileStatement()
            elif(nextToken[0] == "do"):
                self.doStatement()
            elif(nextToken[0] == "return"):
                returnType = self.getFunctionInfo()[1]
                self.returnStatement(returnType)
                self.unreachableCode = True
                self.hasReturnStatement = True

            nextToken = self.lexer.peekNextToken()
        if(self.hasReturnStatement == False):
            self.error(nextToken,"Not all code paths return a value")
        nextToken = self.lexer.getNextToken()
        if(nextToken[0] == "}"):
            # do nothing, we are happy
            self.unreachableCode = False
            self.acceptToken(nextToken)
        else:
            self.error(nextToken,"Expected }")

    def statement(self):
        if(self.printFuncNames):
            print("statement")
        nextToken = self.lexer.peekNextToken()
        if(nextToken[0] == "var"):
            self.varDeclarStatement()
        elif(nextToken[0] == "let"):
            self.letStatement()
        elif(nextToken[0] == "if"):
            self.ifStatement()
        elif(nextToken[0] == "while"):
            self.whileStatement()
        elif(nextToken[0] == "do"):
            self.doStatement()
        elif(nextToken[0] == "return"):
            returnType = self.getFunctionInfo()[1]
            self.returnStatement(returnType)
            self.unreachableCode = True
        else:
            self.error(nextToken," Expected statement")

    def varDeclarStatement(self):
        varName = ""
        varType = ""
        varKind = ""
        if(self.printFuncNames):
            print("varDeclarStatement")

        nextToken = self.lexer.getNextToken()
        if(nextToken[0] == "var"):
            # do nothing, we are happy
            self.acceptToken(nextToken)
            varKind = nextToken[0]
        else:
            self.error(nextToken," Expected var")

        nextToken = self.lexer.getNextToken()
        if(nextToken[0] in ["int","char","boolean","void"] or nextToken[1] == "identifier"):
            # do nothing, we are happy
            self.acceptToken(nextToken)
            varType = nextToken[0]
        else:
            self.error(nextToken," Expected type or identifier (2)")

        nextToken = self.lexer.getNextToken()
        if(nextToken[1] == "identifier"):
            # do nothing, we are happy
            self.acceptToken(nextToken)
            varName = nextToken[0]

        else:
            self.error(nextToken)

        # now we add all the info to the symbol table
        varID = self.findMaxID(self.methodSymbolTable[self.currentSubroutine],varKind)
        self.methodSymbolTable[self.currentSubroutine].append([varName,varType,varKind,varID,False,self.currentClass])

        # check we haven't used this variable name before
        self.checkOnlyUsedOnce(nextToken,"subroutine")

        nextToken = self.lexer.getNextToken()
        while(nextToken[0] == ","):
            self.acceptToken(nextToken)
            nextToken = self.lexer.getNextToken()
            if(nextToken[1] == "identifier"):
                self.acceptToken(nextToken)
                varName = nextToken[0]

            else:
                self.error(nextToken," Expected identifier")

            # now we add the next element to the symbol table
            varID = self.findMaxID(self.methodSymbolTable[self.currentSubroutine],varKind)
            self.methodSymbolTable[self.currentSubroutine].append([varName,varType,varKind,varID,False,self.currentClass])

            # check we haven't used this variable name before
            self.checkOnlyUsedOnce(nextToken,"subroutine")

            nextToken = self.lexer.getNextToken()

        if(nextToken[0] == ";"):
            # do nothing, we are happy
            self.acceptToken(nextToken)
        else:
            self.error(nextToken," Expected ;")

    def letStatement(self):

        leftHandSideType = ""
        leftHandSideVariable = ""
        isArray = False

        if(self.printFuncNames):
            print("letStatement")
        nextToken = self.lexer.getNextToken()
        if(nextToken[0] == "let"):
            # do nothing, we are happy
            self.acceptToken(nextToken)
        else:
            self.error(nextToken," Expected let")


        nextToken = self.lexer.getNextToken()
        if(nextToken[1] == "identifier"):
            # do nothing, we are happy
            self.checkDeclared(nextToken)
            leftHandSideType = self.findVariableType(self.currentClass,self.currentSubroutine,nextToken)
            leftHandSideVariable = nextToken
            self.acceptToken(nextToken)
        else:
            self.error(nextToken," Expected identifier")

        # Initialise variable
        for var in self.methodSymbolTable[self.currentSubroutine]:
            if var[0] == nextToken[0]:
                var[4] = True # now it is initalised
        # if it is not found here then it is just a global,
        # so can't be inialised anyway


        # a zero to one check so is allowed to fail
        nextToken = self.lexer.getNextToken()
        if(nextToken[0] == "["):
            # do nothing, we are happy
            self.acceptToken(nextToken)
            nextToken = self.lexer.peekNextToken()
            if(nextToken[0] in ["-","~","[","(","true","false","null","this"] or nextToken[1] in ["integerConstant","identifier","stringLiteral"]):
                # now we do an expression, that must equate to an integer
                self.expression("int")
            else:
                self.error(nextToken," Expected expression")

            nextToken = self.lexer.getNextToken()
            if(nextToken[0] == "]"):
                # do nothing, we are happy"
                self.acceptToken(nextToken)
            else:
                self.error(nextToken," Expected ]")

            nextToken = self.lexer.getNextToken()

            # code generation
            self.vmCode.append(["push"] + self.vmCodeInfo(leftHandSideVariable))
            self.vmCode.append(["add"])
            isArray = True # since it has a different ending

        if(nextToken[0] == "="):
            # do nothing, we are happy
            self.acceptToken(nextToken)
        else:
            self.error(nextToken," Expected =")
        nextToken = self.lexer.peekNextToken()
        if(nextToken[0] in ["-","~","[","(","true","false","null","this"] or nextToken[1] in ["integerConstant","identifier","stringLiteral","charLiteral"]):
            self.expression(leftHandSideType)
        else:
            self.error(nextToken," Expected expression")

        nextToken = self.lexer.getNextToken()
        if(nextToken[0] == ";"):
            # do nothing, we are happy
            self.acceptToken(nextToken)
        else:
            self.error(nextToken,"Expected ; ")

        # code generation
        if(isArray):
            self.vmCode.append(["pop","temp",0])
            self.vmCode.append(["pop","pointer",1])
            self.vmCode.append(["push","temp",0])
            self.vmCode.append(["pop","that",0])
        else:
            self.vmCode.append(["pop"] + self.vmCodeInfo(leftHandSideVariable))

    def ifStatement(self):
        if(self.printFuncNames):
            print("ifStatement")

        # these parts are used for checking if all
        # code paths return a value
        firstBranchReturns = False
        secondBranchReturns = False
        nextToken = self.lexer.getNextToken()
        if(nextToken[0] == "if"):
            self.acceptToken(nextToken)
        else:
            self.error(nextToken," Expected if")
        # now get the open bracket
        nextToken = self.lexer.getNextToken()
        if(nextToken[0] == "("):
            self.acceptToken(nextToken)
        else:
            self.error(nextToken," Expected (")

        # now get the part inside the if statement
        nextToken = self.lexer.peekNextToken()
        if(nextToken[0] in ["-","~","[","(","true","false","null","this"] or nextToken[1] in ["integerConstant","identifier","stringLiteral","charLiteral"]):
            self.expression("") # we do not know what the type will be
        else:
            self.error(nextToken," Expected expression")

        # now get the closing bracket
        nextToken = self.lexer.getNextToken()
        if(nextToken[0] == ")"):
            self.acceptToken(nextToken)
        else:
            self.error(nextToken," Expected )")

        # code generation
        trueLabel = "IF_TRUE" + str(self.ifTrueCounter)
        falseLabel = "IF_FALSE" + str(self.ifFalseCounter)
        self.ifTrueCounter += 1
        self.ifFalseCounter += 1
        ifEndCounter = self.ifTrueCounter - 1

        self.vmCode.append(["if-goto",trueLabel])
        self.vmCode.append(["goto",falseLabel])
        self.vmCode.append(["label",trueLabel])

        # now get the opening curly bracer
        nextToken = self.lexer.getNextToken()
        if(nextToken[0] == "{"):
            self.acceptToken(nextToken)
        else:
            self.error(nextToken," Expected {")

        # keep accepting statements until it ends
        nextToken = self.lexer.peekNextToken()
        while(nextToken[0] in ["var","let","if","while","do","return"]):
            if(nextToken[0] == "return"):
                firstBranchReturns = True
            if(nextToken[0] == "if"): # hijack the if statement early
                if(self.ifStatement()):# so we can check if all code paths return a value
                        firstBranchReturns = True
            else:
                self.statement()
            nextToken = self.lexer.peekNextToken()

        # now get the closing curly bracer
        nextToken = self.lexer.getNextToken()
        if(nextToken[0] == "}"):
            self.unreachableCode = False
            self.acceptToken(nextToken)
        else:
            self.error(nextToken,"Expected }")


        # now get the closing curly bracer
        nextToken = self.lexer.peekNextToken()
        if(nextToken[0] == "else"):

            # code generation
            endLabel = "IF_END" + str(ifEndCounter)
            self.vmCode.append(["goto",endLabel])
            self.vmCode.append(["label",falseLabel])

            nextToken = self.lexer.getNextToken()
            self.acceptToken(nextToken)

            # now get the opening curly bracer
            nextToken = self.lexer.getNextToken()


            if(nextToken[0] == "{"):
                self.acceptToken(nextToken)
            else:
                self.error(nextToken," Expected {")

            # keep accepting statements until it ends
            nextToken = self.lexer.peekNextToken()
            while(nextToken[0] in ["var","let","if","while","do","return"]):
                if(nextToken[0] == "return"):
                    secondBranchReturns = True
                if(nextToken[0] == "if"): # hijack the if statement early
                    if(self.ifStatement()):# so we can check if all code paths return a value
                        secondBranchReturns = True
                else:
                    self.statement()
                nextToken = self.lexer.peekNextToken()

            # now get the closing curly bracer
            nextToken = self.lexer.getNextToken()
            if(nextToken[0] == "}"):
                self.unreachableCode = False
                self.acceptToken(nextToken)
            else:
                self.error(nextToken,"Expected }")

            # code generation
            self.vmCode.append(["label",endLabel])
        else:
            # gode generation
            self.vmCode.append(["label",falseLabel])
        # now we return 'True' if both parts of the if statement
        # return a value.
        if(firstBranchReturns and secondBranchReturns):
            return True
        return False

    def whileStatement(self):
        # add the label to our vm code
        # code generation
        startLabel = "WHILE_EXP" + str(self.whileCounter)
        self.vmCode.append(["label",startLabel])
        self.whileCounter += 1;
        if(self.printFuncNames):
            print("whileStatement")

        nextToken = self.lexer.getNextToken()
        if(nextToken[0] == "while"):
            self.acceptToken(nextToken)

        else:
            self.error(nextToken," Expected while")
        # now get the open bracket
        nextToken = self.lexer.getNextToken()
        if(nextToken[0] == "("):
            self.acceptToken(nextToken)
        else:
            self.error(nextToken," Expected (")

        # now get the part inside the while statement
        nextToken = self.lexer.peekNextToken()
        if(nextToken[0] in ["-","~","[","(","true","false","null","this"] or nextToken[1] in ["integerConstant","identifier","stringLiteral","charLiteral"]):
            self.expression("") # we do not know what the type will be
        else:
            self.error(nextToken," Expected expression")

        # now get the closing bracket
        nextToken = self.lexer.getNextToken()
        if(nextToken[0] == ")"):
            self.acceptToken(nextToken)
        else:
            self.error(nextToken," Expected )")
        # code generation
        self.vmCode.append(["not"])
        endLabel = "WHILE_END" + str(self.whileEndCounter)
        self.whileEndCounter += 1
        self.vmCode.append(["if-goto",endLabel])
        # now get the opening curly bracer
        nextToken = self.lexer.getNextToken()
        if(nextToken[0] == "{"):
            self.acceptToken(nextToken)
        else:
            self.error(nextToken," Expected {")

        # keep accepting statements until it ends
        nextToken = self.lexer.peekNextToken()
        while(nextToken[0] in ["var","let","if","while","do","return"]):
            self.statement()
            nextToken = self.lexer.peekNextToken()

        # now get the closing curly bracer
        nextToken = self.lexer.getNextToken()
        if(nextToken[0] == "}"):
            self.unreachableCode = False
            self.acceptToken(nextToken)
        else:
            self.error(nextToken,"Expected }")
        #code generation
        self.vmCode.append(["goto",startLabel])
        self.vmCode.append(["label",endLabel])

    def doStatement(self):
        if(self.printFuncNames):
            print("doStatement")
        nextToken = self.lexer.getNextToken()
        if(nextToken[0] == "do"):
            # we are happy because we have accepted the tokens
            self.acceptToken(nextToken)

            # once we have accepted the 'do' we call the subroutineCall
            self.subroutineCall()

            nextToken = self.lexer.getNextToken()

            if(nextToken[0] == ";"):
                # we are happy
                self.acceptToken(nextToken)
            else:
                self.error(nextToken," Expected ;")

        else:
            self.error(nextToken," Expected do")

        # code Generation
        self.vmCode.append(["pop","temp",0])

    def subroutineCall(self):
        if(self.printFuncNames):
            print("subroutineCall")
        nextToken = self.lexer.getNextToken()
        firstPart = nextToken
        secondPart = ""
        if(nextToken[1] == "identifier"):
            # we are happy because we have accepted the tokens
            self.acceptToken(nextToken)

            nextToken = self.lexer.getNextToken()

            # can have a dot, but we don't need one
            if(nextToken[0] == "."):
                self.acceptToken(nextToken)

                nextToken = self.lexer.getNextToken()

                if(nextToken[1] == "identifier"):
                    self.acceptToken(nextToken)
                    secondPart = nextToken
                    nextToken = self.lexer.getNextToken()

                else:
                    # give an error, because a . should be followed
                    # by an identifier
                    self.error(nextToken," Expected identifier")

            # must be an open bracket
            if(nextToken[0] == "("):
                self.acceptToken(nextToken)
                # try statements used to check if refering to current class,
                # handles error when another class is referred to
                try:
                    # code generation
                    # changes depending on weather it is a method or a function
                    className = self.findVariableType(self.currentClass,self.currentSubroutine,firstPart)
                    if(firstPart[0]) != className:
                        self.vmCode.append(["push"] + self.vmCodeInfo(firstPart))
                    else:
                        pass
                except:
                    pass

                if(secondPart == ""):
                    # code generaion, before the arguments
                    self.vmCode.append(["push","pointer","0"]) # put the 'this'

                numberOfArguments = self.expressionList()

                # we have to check at the end weather the functions
                # exist and if the number of arguments are correct,
                # since we cannot check at the moment weather the functions
                # are real
                # just a normal function
                # code generaion
                if(secondPart == ""):
                    self.assertions.append(["exists",self.currentClass,True,firstPart[0],firstPart[2]])
                    self.assertions.append(["numberOfArguments",self.currentClass,firstPart[0],numberOfArguments,firstPart[2]])

                    self.vmCode.append(["call",self.currentClass + "." + firstPart[0],1]) # extra arg for this
                # a function from another class
                else:
                    className = self.findVariableType(self.currentClass,self.currentSubroutine,firstPart)
                    self.assertions.append(["exists",className,True,secondPart[0],firstPart[2]])
                    self.assertions.append(["numberOfArguments",className,secondPart[0],numberOfArguments,firstPart[2]])
                    if(firstPart[0] != className):
                        self.vmCode.append(["call",className + "." + secondPart[0],1])
                        # this has the extra argument of self, since  something.function() needs a arg for what 'something' is
                    else:
                        self.vmCode.append(["call",className + "." + secondPart[0],0])

                nextToken = self.lexer.getNextToken()
                if(nextToken[0] == ")"):
                    self.acceptToken(nextToken)
                else:
                    self.error(nextToken," Expected )")

            else:
                self.error(nextToken," Expected (")

        else:
            self.error(nextToken," Expected identifier")

    def expressionList(self):
        if(self.printFuncNames):
            print("expressionList")

        numberOfExpressions = 0
        nextToken = self.lexer.peekNextToken()
        if(nextToken[0] in ["-","~","(","true","false","null","this"] or nextToken[1] in ["integerConstant","identifier","stringLiteral","charLiteral"]):
            numberOfExpressions += 1
            self.expression("") # can be any type
        else:
            # this is still fine, we just return, since expressionList
            # can just be epsilon
            return 0

        nextToken = self.lexer.peekNextToken()
        if(nextToken[0] == ","):
            nextToken = self.lexer.getNextToken()
            self.acceptToken(nextToken)
            numberOfExpressions += self.expressionList()

        # we are still happy if there is nothing here
        # because an expression list can only have one thing
        return numberOfExpressions

    def returnStatement(self,expectedType):
        if(self.printFuncNames):
            print("returnStatement")
        nextToken = self.lexer.getNextToken()
        if(nextToken[0] == "return"):
            # do nothing, we are happy
            self.acceptToken(nextToken)
        else:
            self.error(nextToken," Expected return")

        nextToken = self.lexer.peekNextToken()
        if(nextToken[0] in ["-","~","(","true","false","null","this"] or nextToken[1] in ["integerConstant","identifier","stringLiteral","charLiteral"]):
            self.expression(expectedType)

        nextToken = self.lexer.getNextToken()
        if(nextToken[0] == ";"):
            # do nothing, we are happy
            self.acceptToken(nextToken)
        else:
            self.error(nextToken," Expected ;")

        # code generation
        if(self.inVoidFunction):
            self.vmCode.append(["push","constant","0"])
        self.vmCode.append(["return"])

    def expression(self,expectedType):
        expressionType = ""
        if(self.printFuncNames):
            print("expression")
        nextToken = self.lexer.peekNextToken()
        expressionType = self.relationalExpression(expectedType)

        # now we have a zero to many relationship
        nextToken = self.lexer.peekNextToken()
        while( nextToken[0] in ["&","|"]):
            vmLine = []
            if(nextToken[0] == "&" or nextToken[0] == "|"):
                # do nothing we are happy
                nextToken = self.lexer.getNextToken()
                self.acceptToken(nextToken)
                if(nextToken[0] == "&"):
                    vmLine = ["and"]
                else:
                    vmLine = ["or"]
                nextToken = self.lexer.peekNextToken()

            expressionType = self.relationalExpression(expectedType)

            # code generation
            if(vmLine != []):
                self.vmCode.append(vmLine)

            nextToken = self.lexer.peekNextToken()

        return expressionType

    def relationalExpression(self,expectedType):
        expressionType = ""
        if(self.printFuncNames):
            print("relationalExpression")
        nextToken = self.lexer.peekNextToken()

        if(nextToken[0] in ["-","~","(","true","false","null","this"] or nextToken[1] in ["integerConstant","identifier","stringLiteral","charLiteral"]):
            expressionType = self.arithmeticExpression(expectedType)
        else:
            self.error(nextToken," Expected arithmeticExpression")

        # now we can have zero to many of more statments
        nextToken = self.lexer.peekNextToken()
        while( nextToken[0] in ["=",">","<"]):
            vmLine = []
            if(nextToken[0] in ["=",">","<"]):
                # code generation
                if(nextToken[0] == "="):
                    vmLine = ["eq"]
                if(nextToken[0] == "<"):
                    vmLine = ["lt"]
                if(nextToken[0] == ">"):
                    vmLine = ["gt"]
                nextToken = self.lexer.getNextToken() # same as the peeked one, but now we have it for real
                self.acceptToken(nextToken)
                nextToken = self.lexer.peekNextToken()
            #if(nextToken[0] in ["-","~","(","true","false","null","this"] or nextToken[1] in ["integerConstant","identifier","stringLiteral","charLiteral"]):
            expressionType = self.arithmeticExpression(expectedType)
            #else:
            #    self.error(nextToken," Expected arithmeticExpression or '=' or '>' or '<'")
            # code generation
            if(vmLine != []):
                self.vmCode.append(vmLine)
            nextToken = self.lexer.peekNextToken()

        return expressionType

    def arithmeticExpression(self,expectedType):
        expressionType = ""
        if(self.printFuncNames):
            print("arithmeticExpression")
        nextToken = self.lexer.peekNextToken()
        if(nextToken[0] in ["-","~","(","true","false","null","this"] or nextToken[1] in ["integerConstant","identifier","stringLiteral","charLiteral"]):
            expressionType = self.term(expectedType)
        else:
            self.error(nextToken," Expected term")

        nextToken = self.lexer.peekNextToken()

        while(nextToken[0] in ["+","-"]):
            vmLine = []


            nextToken = self.lexer.getNextToken()
            self.acceptToken(nextToken)

            # code generation
            if(nextToken[0] == "+"):
                vmLine = ["add"]

            else:
                vmLine = ["sub"]

            expressionType = self.term(expectedType)

            ## code generation
            nextToken = self.lexer.peekNextToken()
            if(vmLine != []):
                self.vmCode.append(vmLine)

        return expressionType

    def term(self,expectedType):
        expressionType = ""
        if(self.printFuncNames):
            print("term")
        nextToken = self.lexer.peekNextToken()
        if(nextToken[0] in ["-","~","(","true","false","null","this"] or nextToken[1] in ["integerConstant","identifier","stringLiteral","charLiteral"]):
            expressionType = self.factor(expectedType)
        else:
            self.error(nextToken," Expected factor")

        nextToken = self.lexer.peekNextToken()

        while(nextToken[0] in ["*","/"]):
            vmLine = []
            nextToken = self.lexer.getNextToken()
            self.acceptToken(nextToken)
            # code generation
            if(nextToken[0] == "*"):
                vmLine = ["call","Math.multiply",0] # put in args as 0, they get fixed later
            else:
                vmLine = ["call","Math.divide",0]

            expressionType = self.factor(expectedType)


            # code generation
            if(vmLine != []):
                self.vmCode.append(vmLine)
            nextToken = self.lexer.peekNextToken()

        return expressionType

    def factor(self,expectedType):
        expressionType = ""
        if(self.printFuncNames):
            print("factor")
        nextToken = self.lexer.peekNextToken()
        vmLine = []
        while(nextToken[0] in ["-","~"]):
            nextToken = self.lexer.getNextToken()
            self.acceptToken(nextToken)
            if(nextToken[0] == "-"):
                nextToken = self.lexer.peekNextToken()
                vmLine.append(["neg"])
            else:
                nextToken = self.lexer.peekNextToken()

                vmLine.append(["not"])

        expressionType = self.operand(expectedType)


        # code generation
        if(vmLine != []):
            vmLine.reverse() # needs to reverse to maintain order of operations
            self.vmCode = self.vmCode + vmLine

        return expressionType

    def operand(self,expectedType):
        expressionType = ""
        if(self.printFuncNames):
            print("operand")
        nextToken = self.lexer.getNextToken()
        # special case for identifiers
        if(nextToken[1] == "identifier"):
            self.acceptToken(nextToken)
            # from here, we can either have
            # 1. A normal variable
            # 2. An array
            # 3. A function call
            # 4. A variable from another class
            # 5. An array from another class
            # 6. A function from another class
            firstPart = nextToken # could be a variable, class.variable, or class.function
            secondPart = ""
            nextToken = self.lexer.peekNextToken()
            if(nextToken[0] == "."):
                # now we either have a class.variable
                # or a                 class.function
                nextToken = self.lexer.getNextToken()
                self.acceptToken(nextToken)
                nextToken = self.lexer.getNextToken()
                if(nextToken[1] == "identifier"):

                    self.acceptToken(nextToken)
                    secondPart = nextToken
                    # now we encounter a variable from a different class,
                    # we will have to check at the end if the type is correct
                    nextToken = self.lexer.peekNextToken()
                else:
                    self.error(nextToken," Expected identifier")
            # now we have the first part, and an optional second part
            # now we can check the three cases, for either a function call
            # an array, or just a normal variable.
            # If they are in another class, we will have to check if they exist
            # at the end of parsing, as we may not have encountered them yet.

            # is a function call
            if(nextToken[0] == "("):
                nextToken = self.lexer.getNextToken()
                # now we check if the function is defined or not
                self.acceptToken(nextToken)
                try:
                    className = self.findVariableType(self.currentClass,self.currentSubroutine,firstPart)
                    if(firstPart[0]) != className:
                        self.vmCode.append(["push"] + self.vmCodeInfo(firstPart))
                    else:
                        pass
                except:
                    pass

                numberOfArguments = self.expressionList()

                # we have to check at the end weather the functions
                # exist and if the number of arguments are correct,
                # since we cannot check at the moment weather the functions
                # are real
                # just a normal function
                if(secondPart == ""):
                    self.assertions.append(["exists",self.currentClass,True,firstPart[0],firstPart[2]])
                    self.assertions.append(["typeCheck",self.currentClass,True,firstPart[0],expectedType,firstPart[2]])
                    self.assertions.append(["numberOfArguments",self.currentClass,firstPart[0],numberOfArguments,firstPart[2]])
                    self.vmCode.append(["call",self.currentClass + "." + firstPart[0],0])
                # a function from another class
                else:
                    className = self.findVariableType(self.currentClass,self.currentSubroutine,firstPart)
                    self.assertions.append(["exists",className,True,secondPart[0],firstPart[2]])
                    self.assertions.append(["typeCheck",className,True,secondPart[0],expectedType,firstPart[2]])
                    self.assertions.append(["numberOfArguments",className,secondPart[0],numberOfArguments,firstPart[2]])
                    if(firstPart[0] != className):
                        self.vmCode.append(["call",className + "." + secondPart[0],1])
                        # this has the extra argument of self, since  something.function() needs a arg for what 'something' is
                    else:
                        self.vmCode.append(["call",className + "." + secondPart[0],0])
                nextToken = self.lexer.getNextToken()
                if(nextToken[0] == ")"):
                    # do nothing, we are happy
                    self.acceptToken(nextToken)
                else:
                    self.error(nextToken,"Expected )")
            # is an array
            elif(nextToken[0] == "["):
                nextToken = self.lexer.getNextToken()
                # do nothing, we are happy
                self.acceptToken(nextToken)
                # now we check that the variable exists

                # just a local variable
                if(secondPart == ""):
                    self.checkDeclared(firstPart)
                    self.checkInitlised(firstPart)

                # a variable from another class
                else:
                    className = self.findVariableType(self.currentClass,self.currentSubroutine,firstPart)
                    self.assertions.append(["exists",className,False,secondPart[0],firstPart[2]])
                    self.assertions.append(["typeCheck",className,False,secondPart[0],expectedType,firstPart[2]])
                    expressionType = ""


                # here we check that the expression is of type 'int'
                # if not, we will get an error
                self.expression("int")

                # code generation
                self.vmCode.append(["push"] + self.vmCodeInfo(firstPart))
                self.vmCode.append(["add"])
                self.vmCode.append(["pop","pointer",1])
                self.vmCode.append(["push","that",0])

                nextToken = self.lexer.getNextToken()
                if(nextToken[0] == "]"):
                    # do nothing, we are happy
                    self.acceptToken(nextToken)
                else:
                    self.error(nextToken," Expected ]")

            # Just a variable
            else:
                # just a variable from this class
                if(secondPart == ""):
                    self.checkDeclared(firstPart)
                    self.checkInitlised(firstPart)
                    expressionType = self.findVariableType(self.currentClass,self.currentSubroutine,firstPart)
                    self.vmCode.append(["push"]+self.vmCodeInfo(firstPart))

                # a variable from another class
                else:
                    className = self.findVariableType(self.currentClass,self.currentSubroutine,firstPart)
                    self.assertions.append(["exists",className,False,secondPart[0],firstPart[2]])
                    self.assertions.append(["typeCheck",className,False,secondPart[0],expectedType,firstPart[2]])
                    expressionType = expectedType # just assumes it works until the end where we check

        elif(nextToken[0] == "("):
            self.acceptToken(nextToken)

            # now get the part inside the brackets
            nextToken = self.lexer.peekNextToken()
            if(nextToken[0] in ["-","~","[","(","true","false","null","this"] or nextToken[1] in ["integerConstant","identifier","stringLiteral","charLiteral"]):
                self.expression(expectedType) # we do not know what the type will be
            else:
                self.error(nextToken," Expected expression")

            # now get the closing bracket
            nextToken = self.lexer.getNextToken()
            if(nextToken[0] == ")"):
                self.acceptToken(nextToken)
            else:
                self.error(nextToken," Expected )")

        elif(nextToken[0] in ["true","false","null","this"] or nextToken[1] in ["integerConstant","stringLiteral","charLiteral"]):
            if(nextToken[1] == "integerConstant"):
                expressionType = "int"
                # code generation
                self.vmCode.append(["push","constant",str(nextToken[0])])
            elif(nextToken[1] == "stringLiteral"):
                expressionType = "String"
                # code generation

                self.vmCode.append(["push","constant",len(nextToken[0])])
                self.vmCode.append(["call","String.new",0])  # correct args done later
                for letter in nextToken[0]:
                    self.vmCode.append(["push","constant",ord(letter)])
                    self.vmCode.append(["call","String.appendChar",1]) # correct args done later
            elif(nextToken[0] == "true" or nextToken[0] == "false"):
                expressionType = "boolean"
                # code generation
                self.vmCode.append(["push","constant",0])
                if(nextToken[0] == "true"): # do 'not' if it's true
                    self.vmCode.append(["not"])
            elif(nextToken[0] == "this"):
                # since 'this' always refers to the class it is in
                expressionType = self.currentClass
                # code generation
                self.vmCode.append(["push","pointer","0"])
            elif(nextToken[1] == "charLiteral"): # because chars are just ints
                expressionType = "int"
                # code generation
                # todo
            self.acceptToken(nextToken)
        else:
            self.error(nextToken,"Expected operand")

        # only check if we have found the expressions type
        # if we haven't found it yet, it will be checked at the end
        # have special case for arrays, because they are Different
        if(expectedType == "Array"):
            expressionType = ""
        if(expressionType != "" and expectedType != "" and expectedType != expressionType):
            self.error(nextToken,"Mismatching types in expression:\n Expected " + str(expectedType) + " instead got " + str(expressionType))
        return expressionType

    def parse(self):
        self.displayMessage("Parsing: " + self.fileName)
        # reset method table, so we can have functions with the same name
        self.methodSymbolTable = {}
        self.vmCode = []
        self.classDeclar()

        # return statements, for the info to the compielr
        return self.classSymbolTable,self.methodSymbolTable,self.assertions,self.classMethods,self.vmCode
