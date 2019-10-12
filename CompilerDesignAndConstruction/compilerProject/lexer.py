#import statements
import sys,time,language,numbers,string


class Lexer:
    """ This is the class that contains all the neccassary functions
        for the parser to run, to use call Parser.lexicalAnalysis() """

    # this is the input code, this is used to give line numbers to errors
    rawSourceCode = ""

    # used only for checking the line number
    refinedSourceCode = ""
    lineNumber = 0

    # used for get next token
    tokenCounter = 0
    splitCode = ""
    finalTokenList = []

    # used at the end, so we know where to save the file to
    globalFileName = ""

    # will either give a warning, or will terminate the program
    exitOnErrors = False

    def openfile(self,filename="None"):
        """ opens the file provided by the Command Line Arguments,
            if there are none provided. We willl open the file browser,
            which allows the user to select a .JACK file """
        if(filename == "None"):
            # if the user has not given a file to open from the command line
            # then a dialogue will open asking them to select the source file
            self.displayMessage("Error: Please provide a file path ",True)
            filename = askopenfilename()
        #print("Opened ",filename)
        # atttempts at opening the file
        try:
            textFile = open(filename,"r")
        except:
            self.displayMessage("Invalid File",True)
        # so we know what to save the file as later

        self.globalFileName = filename.split("/")[-1]
        self.globalFileName = self.globalFileName.split(".")[:-1] #removes the file extension
        self.globalFileName = "".join(self.globalFileName)
        # upates the rawsourcecode in the class
        self.rawSourceCode = textFile.read()

    def getCommandLineArguments(self):
        """ This function will look to see if the user
            has ran the program with a filename, if they
            have, the program will attempt to read the file"""
        if(len(sys.argv) == 1):
            return "None"
        return (sys.argv[1])

    def removeComments(self,code):
        """ Simply takes the code, removing the multi line Comments
            and the standard comments aswell """

        # output string
        codeWithoutComments = ""

        # standard comment
        isComment = False

        # multi line comments have to be different
        isMultiComment = False

        # go through regular code
        for i in range(len(code)):
            if(code[i] == "/"):
                 # standard comment
                if(code[i+1] == "/" and isMultiComment == False):
                    # can only be a comment if we are not already in one
                    isComment = True
                # multi line comment
                if(code[i+1] == "*" and isComment == False):
                    # can only be a comment if we are not already in one
                    isMultiComment = True
            elif(code[i] == "*"):
                # ending a multi line comment
                if(code[i+1] == "/" and isComment == False):
                    # can only be the end of a multi, if we are not alredy in one
                    isMultiComment = False
                    # this part just removes the end of the comment
                    code = code[:i] + "  " + code[i+2:]
            # every new line means we are no longer in a comment
            elif(code[i] == "\n"):
                if(isMultiComment == False):
                    isComment = False
            # add the code to the new section if we are not in a comment
            if(isComment == False and isMultiComment == False):
                codeWithoutComments += code[i]
        #print("Removed Comments")
        self.refinedSourceCode = codeWithoutComments

    def tokenize(self,code):
        """ This takes our code, with comments removed, and
            catogarises each lexeme, and formats it in XML"""
        # will be written to file, always starts with <tokens>
        output = "<tokens>\n"

        # this function splits up the code
        self.splitCode = self.splitUpCode(code)

        # takes the split code
        for i in range(len(self.splitCode)):

            oldLineNumber = self.lineNumber
            try:
                while(self.splitCode[i] not in self.rawSourceCode.split("\n")[self.lineNumber]):
                    self.lineNumber+=1
            except:
                # this is for the case where strings do not rejoin properly
                # but does not effect actual running
                self.lineNumber = oldLineNumber


            # keywords must be followed by a space, so check for that first
            if((self.splitCode[i] + " ") in language.language):
                token = language.language[self.splitCode[i] + " "]

            # if not, check if it is a symbol, which do not need spaces
            elif((self.splitCode[i]) in language.language):
                token = language.language[self.splitCode[i]]

            # might be a string literal or a variable or something so check that
            else:
                token,self.splitCode[i] = self.catogariseToken(self.splitCode[i])

            self.finalTokenList.append([self.splitCode[i],token,self.lineNumber+1])
            output += "<" + token + "> " + self.splitCode[i] + " </" + token + ">\n"
        output += "</tokens>\n"
        #print("Tokenized")

        # resets this, so that we can still use get next token later
        self.lineNumber = 0

        # writes to file
        self.saveOutput(output)

    def getNextToken(self):
        """ This gives out the next token, which will be used
            by the parser """
        try:
            returnToken = self.finalTokenList[self.tokenCounter]
            #print("Token: ",returnToken)
        except:
            self.displayMessage("Unexpected EOF while parsing\n Check for balanced brackets",True)
        self.tokenCounter += 1
        return returnToken

    def peekNextToken(self,peek=False):
        """ This gives out the next token, but does not incremenet """
        try:
            returnToken = self.finalTokenList[self.tokenCounter]
        except:
            self.displayMessage("Unexpected EOF while parsing\n Check for balanced brackets",True)
        return returnToken

    def catogariseToken(self,lexeme):
        """ This function is ran whenever we have a lexeme,
            it is not a symbol or keyword, so we must determine
            if it is a char, string, int or a identifier """

        # default
        token = "identifier"

        # check weather the token is an integer
        try:
            int(lexeme) # this check will fail if the lexeme is not an integer
            token = "integerConstant"
            # does not need checking since is just an int, so we return
            return token,lexeme
        except:
            # check for string
            if(lexeme[0] == '"'):
                token = "stringLiteral"
                if(lexeme[-1] != '"'):
                    self.displayMessage(str("Unexpected EOF While Parsing on line " + str(self.lineNumber+1)
                    + "\n While performing lexical analysis on string literal\n Lexeme: " + lexeme),True)

                lexeme = lexeme[1:-1]
            # check for char
            elif(lexeme[0] == "'"):
                token = "charLiteral"
                if(lexeme[-1] != "'"):
                    self.displayMessage(str("Unexpected EOF While Parsing on line "+ str(self.lineNumber+1)),True)
                lexeme = lexeme[1:-1]


        # then we check that our identifier is valid
        if(token == "identifier"):
            self.identifierCheck(lexeme)
        return token,lexeme

    def identifierCheck(self,lexeme):
        """ This checks that the identifier contains
            only a-z,A-Z, and _ but non first letters can be numbers"""
        if(lexeme[0] not in string.ascii_lowercase     and
           lexeme[0] not in string.ascii_uppercase     and
           lexeme[0] != "_"):

            self.displayMessage(str("Syntax Error: " + str(lexeme) + "\n Error on line " + str(self.lineNumber)),True)

        for letter in lexeme:
            if(letter not in string.ascii_lowercase    and
               letter not in string.ascii_uppercase    and
               letter != "_"                           and
               letter not in ["0","1","2","3","4","5","6","7","8","9"]):
               self.displayMessage(str("Syntax Error: " + str(lexeme) + "\n Error on line " + str(self.lineNumber)),True)

    def saveOutput(self,xmlOutput,filename="None"):
        """ Writes the output to a text file """
        textFile = open("Output/" + self.globalFileName + ".txt","w")
        textFile.write(xmlOutput)
        textFile.close()

    def removeNewLines(self,code):
        """ removes the new lines """
        # output string
        codeWithoutNewlines = ""

        # go through regular code
        for i in range(len(code)):
            if(code[i] != "\n"):
                codeWithoutNewlines = codeWithoutNewlines + code[i]

        self.refinedSourceCode = codeWithoutNewlines

    def splitUpCode(self,code):
        """This function turns the code from a string
            into a list containing one token in each list element

            e.g "class.function()  - - >  ["class",".,"function","(",")"] """

        splitCode = code.split(" ")

        # special case, sort out string literals
        i = 0
        while i < (len(splitCode)):
            for j in range(len(splitCode[i])):
                if(splitCode[i][j] == '"'):
                    k = 1
                    while(j+k < len(splitCode[i]) and splitCode[i][j+k] != '"'):
                        k += 1
                    splitCode = splitCode[:i] + [splitCode[i][:j]] + [splitCode[i][j:j+k+1]] + [splitCode[i][j+k+1:]] + splitCode[i+1:]
                    i += 1
                    break;
            i += 1

        # now we have all the strings seperated put them back together again
        i = 0
        while i < len(splitCode):
            if(len(splitCode[i]) > 0):
                if(splitCode[i][0] == '"' and splitCode[i][-1] != '"'):
                    j = 1
                    while(i+j < len(splitCode)):
                        if(len(splitCode[i+j]) > 0):
                            if(splitCode[i+j][0] == '"'):
                                break;
                        j += 1
                    splitCode = splitCode[:i] + [(" ").join(splitCode[i:i+j] + ['"'])] + [splitCode[i+j][1:]] +splitCode[i+j+1:]
                    i += j
            i += 1

        i = 0
        splitItems = language.splitItems
        for item in splitItems:

            splitCode = self.removeWhiteSpace(splitCode)
            i = 0
            while(i < len(splitCode)):
                if(item in splitCode[i] and item != splitCode[i]):
                    if(splitCode[i][0] == '"' and splitCode[i][-1] == '"'):
                        # don't do it, because we don't need to split things inside  " "
                        i += 1
                        continue;
                    newSplitCode = splitCode[:i]
                    for k in range(len(splitCode[i].split(item))-1):
                        newSplitCode = newSplitCode + [splitCode[i].split(item)[k]] + [item]
                    newSplitCode = newSplitCode + [splitCode[i].split(item)[-1]] + splitCode[i+1:]
                    splitCode = newSplitCode
                    i += 2
                i += 1

        splitCode = self.removeWhiteSpace(splitCode)

        return splitCode

    def removeWhiteSpace(self,listCode):
        # keep on removing the white space, until we get an error
        # removes all the tabs
        for i in range(len(listCode)):
            listCode[i] = listCode[i].strip("\t")
        # removes all the spaces
        try:
            while(True):
                listCode.remove('')
        except:
            pass
        return listCode

    def reset(self):
        """This function puts everything back to what it was like
           before the lexer started, so we can do lexicalAnalysis
           on another file without having to use a new class instance"""
        rawSourceCode = ""
        refinedSourceCode = ""
        lineNumber = 0
        tokenCounter = 0
        splitCode = ""
        finalTokenList = []
        globalFileName = ""
        #print("Reset")

    def displayMessage(self,message,isError=False):
        """ Produces nicely formatted messages for either messages or errors """

        print("---------------------\n",message,"\n---------------------")
        if(isError and self.exitOnErrors):
            sys.exit()
        else:
            print("WARNING")
            time.sleep(1)

    def lexicalAnalysis(self,fileName,exitOnErrors):

        self.exitOnErrors = exitOnErrors
        start = time.time()

        # open the file and put it in the source code
        #self.openfile(self.getCommandLineArguments())
        self.openfile(fileName)

        # remove comments
        self.removeComments(self.rawSourceCode)

        # remove new lines
        self.removeNewLines(self.refinedSourceCode)

        # finally tokenize
        self.tokenize(self.refinedSourceCode)

        # reset all the local vars for next lexical analysis
        self.reset()


        # show time statistics
        #self.displayMessage(str("Time taken " + str(time.time()-start)))
