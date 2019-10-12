    # this is just a dictionary datastructure
# this allows us a seperate store of all the features of the
# language, allowing us to easliy update them, seperate from the program
language = {
    "class "        : "keyword",
    "constructor "  : "keyword",
    "method "       : "keyword",
    "function "     : "keyword",
    "int "          : "keyword",
    "boolean "      : "keyword",
    "char "         : "keyword",
    "void "         : "keyword",
    "var "          : "keyword",
    "static "       : "keyword",
    "field "        : "keyword",
    "let "          : "keyword",
    "do "           : "keyword",
    "if "           : "keyword",
    "else "         : "keyword",
    "while "        : "keyword",
    "return "       : "keyword",
    "true "         : "keyword",
    "false "        : "keyword",
    "null "         : "keyword",
    "this "         : "keyword",
    "(" : "symbol",
    ")" : "symbol",
    "[" : "symbol",
    "]" : "symbol",
    "{" : "symbol",
    "}" : "symbol",
    ";" : "symbol",
    "," : "symbol",
    "=" : "symbol",
    "." : "symbol",
    "+" : "symbol",
    "-" : "symbol",
    "*" : "symbol",
    "/" : "symbol",
    "&" : "symbol",
    "|" : "symbol",
    "~" : "symbol",
    "<" : "symbol",
    ">" : "symbol",
    #"String "       : "keyword",
}

splitItems = [  'boolean ', 'char ', 'class ', 'constructor ',
                'do ', 'else ', 'false ', 'field ', 'function ',
                'if ', 'int ', 'let ', 'method ', 'null ', 'return ',
                'static ', 'this ', 'true ', 'var ', 'void ', 'while ',
                '(', ')','&', '*', '+', ',', '-', '.', '/', ';', '<', '=',
                '>', '[', ']', '{', '|', '}', '~']

# this dictionary should be used for the parser

# for the special characters such as -> ( ) { } []

# these are handled seperately

#  ( )  ==  JACK_Or
#  { }  ==  JACK_One_To_Many
#  [ ]  ==  JACK_Zero_To_One

grammar = {
    "classDeclar" : ["class","identifier","{","JACK_Zero_To_Many","memberDeclar","JACK_Zero_To_Many","}"],
    "memberDeclar" : ["JACK_Or","classVarDeclar","subroutineDeclar","JACK_Or"],
    "classVarDeclar" : ["JACK_Or","static","field","JACK_Or","type","identifier","JACK_Zero_To_Many",",","identifier","JACK_Zero_To_Many",";"],
    "type" : ["JACK_Or","int","char","boolean","identifier","JACK_Or"],
    "subroutineDeclar" : ["JACK_Or","constructor","function","method","JACK_Or","JACK_Or","type","void","JACK_Or","identifier","(","JACK_Or","paramList","JACK_void","JACK_Or",")","subroutineBody"],
    "paramList" : ["type","identifier","JACK_Zero_To_Many",",","type","identifier","JACK_Zero_To_Many"],
    "subroutineBody" : ["{","JACK_Zero_To_Many","statement","JACK_Zero_To_Many","}"],
    "statement" : ["JACK_Or","varDeclarStatement","letStatement","ifStatement","whileStatement","doStatement","returnStatement","JACK_Or"],
    "varDeclarStatement" : ["var","type","identifier","JACK_Zero_To_Many",",","identifier","JACK_Zero_To_Many",";"],
    "letStatement" : ["let","identifier","JACK_Zero_To_One","[","expression","]","JACK_Zero_To_One","=","expression",";"],
    "ifStatement" : ["if","(","expression",")","{","JACK_Zero_To_Many","statement","JACK_Zero_To_Many","}","JACK_Zero_To_One"],
    "whileStatement" : ["while","(","expression",")","{","JACK_Zero_To_Many","statement","JACK_Zero_To_Many","}"],
    "doStatement" : ["do","subroutineCall"],
    "subroutineCall" : ["identifier","JACK_Zero_To_One",".","identifier","JACK_Zero_To_One","(","expressionList",")",";"],
    "expressionList" : ["expression","JACK_Or","JACK_Zero_To_Many",",","expression","JACK_Zero_To_Many","void","JACK_Or"],
    "returnStatement" : ["return","JACK_Zero_To_One","expression","JACK_Zero_To_One",";"],
    "expression" : ["relationalExpression","JACK_Zero_To_Many","JACK_Or","&","|","JACK_Or","relationalExpression","JACK_Zero_To_Many"],
    "relationalExpression" : ["ArithmeticExpression","JACK_Zero_To_Many","JACK_Or","=",">","<","JACK_Or","ArithmeticExpression"],
    "ArithmeticExpression" : ["term","JACK_Zero_To_Many","JACK_Or","+","-","JACK_Or","term","JACK_Zero_To_Many"],
    "term" : ["factor","JACK_Zero_To_Many","JACK_Or","*","/","JACK_Or","factor","JACK_Zero_To_Many"],
    "factor" : ["JACK_Or","-","~","JACK_Or","operand"],
    "operand" : ["JACK_Or","integerConstant","identifier","[","expression","]","subroutineCall","(","expression",")","stringLiteral","true","false","null","this"],
}
