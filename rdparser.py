#PROG --> IMPORTS* CLASS_DECLARATION
#IMPORTS --> 'import' IDENTIFIER
#CLASS_DECLARATION --> 'public class' IDENTIFIER '{' MAIN_METHOD_DECLARATION '}'
#MAIN_METHOD_DECLARATION --> 'public \. static \. void \. main (String[] args) {' METHOD_BODY '}'
#METHOD_BODY --> ASSIGNMENT_CALL | PROCEDURE_CALL | PRINT_STATEMENT | EXIT_STATEMENT | ARITHMETIC_STATEMENT
#ASSIGNMENT_CALL -> 'String' IDENTIFIER | 'String[]' IDENTIFER |  'boolean' IDENTIFER | 'double' IDENTIFIER 
#PRINT_STATEMENT --> 'System.out.println(' ( IDENTIFIER ' ' \+ )+ ';'
#ARITHMETIC_STATEMENT --> 'System.out.println(' ( IDENTIFIER ' ' \+ )+ ';'
#EXIT_STATEMENT --> 'System.exit(0)' ';'
#IDENTIFIER --> [a-zA-Z]+
import sys
import generator as CG
import scanner as SC

currentPosition = 0;

def main():
    sentence = sys.argv[1]

    #scan input
    with open(sys.argv[1], "r") as word_list:
        sentence = word_list.read().split()

    #Remove comments, tabs, spaces, and newlines
    for i in range(len(sentence)-1):

        #Remove whitespace
        if sentence[i] == ' ' or sentence[i] == '\t' or sentence[i] == '\n':
            del sentence[i]
    
    try:
        CG.genProgEntry()
        print("gen prog entry complete")
        prog(sentence);
    except:
        print("Error")

def prog(sentence):
    if(currentPosition == 0):
        #if (sentence[0] == 'import'):
            #imports(sentence)
        #elif (sentence[0] == 'public'):
        if (sentence[0] == 'PublicSym'):
            class_declaration(sentence)
        else:
            terminate(False, sentence[currentPosition])
    else:
        terminate(False, sentence[currentPosition])

def class_declaration(sentence):
    global currentPosition

    if (sentence[currentPosition] == 'PublicSym'):
        currentPosition+=1
        if (sentence[currentPosition] == 'ClassSym'):
            currentPosition+=1
            if (sentence[currentPosition] == 'IdentSym'):
                currentPosition+=1
                #identifier(sentence)
                if (sentence[currentPosition] == 'LCurlSym'):
                    currentPosition+=1
                    main_method_declaration(sentence)
                    if (sentence[currentPosition] == 'RCurlSym'):
                        currentPosition+=1
                        return True
                    else:
                        terminate(False, sentence[currentPosition])
                else:
                    terminate(False, sentence[currentPosition])
            else:
                terminate(False, sentence[currentPosition])
        else:
            terminate(False, sentence[currentPosition])
    else:
        terminate(False, sentence[currentPosition])

def main_method_declaration(sentence):
    global currentPosition

    if (sentence[currentPosition] == 'PublicSym'):
        currentPosition+=1
        if (sentence[currentPosition] == 'StaticSym'):
            currentPosition+=1
            if (sentence[currentPosition] == 'VoidSym'):
                currentPosition+=1
                if (sentence[currentPosition] == 'MainSym'):
                    currentPosition+=1
                    if (sentence[currentPosition] == 'LparenSym'):
                        currentPosition+=1
                        if (sentence[currentPosition] == 'StringSym'):
                            currentPosition+=1
                            if (sentence[currentPosition] == 'ArraySym'):
                                currentPosition+=1
                                if (sentence[currentPosition] == 'ArgsSym'):
                                    currentPosition+=1
                                    if (sentence[currentPosition] == 'RparenSym'):
                                        currentPosition+=1
                                        if (sentence[currentPosition] == 'LCurlSym'):
                                            currentPosition+=1
                                            method_body(sentence)
                                            if (sentence[currentPosition] == 'RCurlSym'):
                                                currentPosition+=1
                                                return True
                                            else:
                                                terminate(False, sentence[currentPosition])
                                        else:
                                            terminate(False, sentence[currentPosition])
                                    else:
                                        terminate(False, sentence[currentPosition])
                                else:
                                    terminate(False, sentence[currentPosition])
                            else:
                                terminate(False, sentence[currentPosition])
                        else:
                            terminate(False, sentence[currentPosition])
                    else:
                        terminate(False, sentence[currentPosition])
                else:
                    terminate(False, sentence[currentPosition])
            else:
                terminate(False, sentence[currentPosition])
        else:
            terminate(False, sentence[currentPosition])
    else:
        terminate(False, sentence[currentPosition])

                                    
#Only handle print statements and exit statements
def method_body(sentence):
    global currentPosition

    if (currentPosition < len(sentence)):
        if (sentence[currentPosition == 'StringSym']) or (sentence[currentPosition == 'DoubleSym']) or (sentence[currentPosition == 'BooleanSym']):
            assignment_call(sentence)
            return True
        elif (sentence[currentPosition] == 'IfSym']):
            if_statement(sentence)
            return True
        elif(sentence[currentPosition] == 'WhileSym']):
            while_loop(sentence)
            return True
        elif(sentence[currentPosition] == 'ForSym']):
            for_loop(sentence)
            return True
        elif (sentence[currentPosition] == 'SystemSym') and (sentence[currentPosition+2] == 'OutSym'):
            print_statement(sentence)
            return True
        elif (sentence[currentPosition] == 'SystemSym') and (sentence[currentPosition+2] == 'ExitSym'):
            end_prog(sentence)
            return True
    else:
        terminate(True, sentence)
        

def assignment_call(sentence):
    if (sentence[currentPosition == 'StringSym']):
        currentPosition+=1
        if (sentence[currentPosition == 'ArraySym']):
            currentPosition+=1
            while (sentence[currentPosition] == 'IdentSym'):
                currentPosition+=1
            if (sentence[currentPosition == 'SemicolonSym']):
                currentPosition+=1
                print("ttt")
                print(SC.args)
                CG.genPrintStatement(SC.args)
                #terminate(True, sentence)
                method_body(sentence)
            if (sentence[currentPosition+1 == 'EqualSym']):
                currentPosition+=2
                while (sentence[currentPosition] == 'IdentSym'):
                    currentPosition+=1
                if (sentence[currentPosition == 'SemicolonSym']):
                    currentPosition+=1
                    print("ttt")
                    print(SC.args)
                    CG.genPrintStatement(SC.args)
                    #terminate(True, sentence)
                    method_body(sentence)
                else:
                    terminate(False, sentence[currentPosition])
            else:
                terminate(False, sentence[currentPosition])

        while (sentence[currentPosition] == 'IdentSym'):
            currentPosition+=1
            if (sentence[currentPosition == 'PeriodSym'):
                currentPosition+=1
                while (sentence[currentPosition] == 'IdentSym'):
                currentPosition+=1
                if (sentence[currentPosition] == 'LparentSym'):
                    currentPosition+=1
                    if (sentence[currentPosition] == 'RparentSym'):
                        currentPosition+=1
                        if (sentence[currentPosition == 'SemicolonSym']):
                            currentPosition+=1
                            print("ttt")
                            print(SC.args)
                            CG.genPrintStatement(SC.args)
                            #terminate(True, sentence)
                            method_body(sentence)
                        else:
                            terminate(False, sentence[currentPosition])
                    else:
                        terminate(False, sentence[currentPosition])
                else:
                    terminate(False, sentence[currentPosition])
            if (sentence[currentPosition == 'SemicolonSym']):
                currentPosition+=1
                print("ttt")
                print(SC.args)
                CG.genPrintStatement(SC.args)
                #terminate(True, sentence)
                method_body(sentence)
            if (sentence[currentPosition+2 == 'EqualSym']):
                currentPosition+=2
                while (sentence[currentPosition] == 'IdentSym'):
                    currentPosition+=1
                if (sentence[currentPosition == 'SemicolonSym']):
                    currentPosition+=1
                    print("ttt")
                    print(SC.args)
                    CG.genPrintStatement(SC.args)
                    #terminate(True, sentence)
                    method_body(sentence)
                else:
                    terminate(False, sentence[currentPosition])
            else:
                terminate(False, sentence[currentPosition])
            
        else:
            terminate(False, sentence[currentPosition])
    if(sentence[currentPosition == 'BooleanSym']):
        currentPosition+=1
        while (sentence[currentPosition] == 'IdentSym'):
            currentPosition+=1
        if (sentence[currentPosition+2 == 'EqualSym']):
            currentPosition+=2
            while (sentence[currentPosition] == 'IdentSym'):
                currentPosition+=1
            if (sentence[currentPosition == 'SemicolonSym']):
                currentPosition+=1
                print("ttt")
                print(SC.args)
                CG.genPrintStatement(SC.args)
                #terminate(True, sentence)
                method_body(sentence)
            else:
                terminate(False, sentence[currentPosition])
        else:
            terminate(False, sentence[currentPosition])
    if(sentence[currentPosition == 'DoubleSym']):
        currentPosition+=1
        while (sentence[currentPosition] == 'IdentSym'):
            currentPosition+=1
            if (sentence[currentPosition == 'PeriodSym'):
                currentPosition+=1
                while (sentence[currentPosition] == 'IdentSym'):
                currentPosition+=1
                if (sentence[currentPosition] == 'LparentSym'):
                    currentPosition+=1
                    if (sentence[currentPosition] == 'RparentSym'):
                        currentPosition+=1
                        if (sentence[currentPosition == 'SemicolonSym']):
                            currentPosition+=1
                            print("ttt")
                            print(SC.args)
                            CG.genPrintStatement(SC.args)
                            #terminate(True, sentence)
                            method_body(sentence)
                        else:
                            terminate(False, sentence[currentPosition])
                    else:
                        terminate(False, sentence[currentPosition])
                else:
                    terminate(False, sentence[currentPosition])
        if (sentence[currentPosition == 'SemicolonSym']):
            currentPosition+=1
            print("ttt")
            print(SC.args)
            CG.genPrintStatement(SC.args)
            #terminate(True, sentence)
            method_body(sentence)
        else:
            terminate(False, sentence[currentPosition])
        
    else:
        terminate(False, sentence[currentPosition])
                

def print_statement(sentence):
    global currentPosition

    if (sentence[currentPosition] == 'SystemSym'):
        currentPosition+=1
        if (sentence[currentPosition] == 'PeriodSym'):
            currentPosition+=1
            if (sentence[currentPosition] == 'OutSym'):
                currentPosition+=1
                if (sentence[currentPosition] == 'PeriodSym'):
                    currentPosition+=1
                    if (sentence[currentPosition] == 'PrintSym'):
                        currentPosition+=1
                        if (sentence[currentPosition] == 'LparenSym'):
                            currentPosition+=1

                            #Java lets you print a string of identifiers
                            while (sentence[currentPosition] == 'IdentSym'):
                                currentPosition+=1
                            if (sentence[currentPosition] == 'RparenSym'):
                                currentPosition+=1
                                if (sentence[currentPosition] == 'SemicolonSym'):
                                    currentPosition+=1
                                    print("ttt")
                                    print(SC.args)
                                    CG.genPrintStatement(SC.args)
                                    #terminate(True, sentence)
                                    method_body(sentence)
                                else:
                                    terminate(False, sentence[currentPosition])
                            else:
                                terminate(False, sentence[currentPosition])
                        else:
                            terminate(False, sentence[currentPosition])
                    else:
                        terminate(False, sentence[currentPosition])
                else:
                    terminate(False, sentence[currentPosition])
            else:
                terminate(False, sentence[currentPosition])
        else:
            terminate(False, sentence[currentPosition])
    else:
        terminate(False, sentence[currentPosition])

def for_loop(sentence):
    global currentPosition

    if (sentence[currentPosition] == 'ForSym'):
        currentPosition+=1
        if (sentence[currentPosition] == 'LbrakSym'):
            currentPosition+=1
            compound_statement(sentence)
            if (sentence[currentPosition] == 'RCurlSym'):
                currentPosition+=1
                return True
            else:
                terminate(False, sentence[currentPosition])
        else:
            terminate(False, sentence[currentPosition])
    else:
        terminate(False, sentence[currentPosition])

def while_loop(sentence):
    global currentPosition

    if (sentence[currentPosition] == 'WhileSym'):
        currentPosition+=1
        if (sentence[currentPosition] == 'LbrakSym'):
            currentPosition+=1
            compound_statement(sentence)
            if (sentence[currentPosition] == 'RCurlSym'):
                currentPosition+=1
                return True
            else:
                terminate(False, sentence[currentPosition])
        else:
            terminate(False, sentence[currentPosition])
    else:
        terminate(False, sentence[currentPosition])

def compound_statement(sentence):
    global currentPosition

    if (sentence[currentPosition] == 'IdentSym' or sentence[currentPosition] == 'NumberSym' ):
        currentPosition+=1
        if (sentence[currentPosition] == 'NeqSym' or sentence[currentPosition] == 'GeqSym' or sentence[currentPosition] == 'LeqSym' or sentence[currentPosition] == 'LssSym' or sentence[currentPosition] == 'GtrSym' or sentence[currentPosition] == 'EqlSym'):
            if (sentence[currentPosition] == 'IdentSym' or sentence[currentPosition] == 'NumberSym' ):
                currentPosition+=1
                return True
            else:
                terminate(False, sentence[currentPosition])
    else:
        terminate(False, sentence[currentPosition])

def if_statement(sentence):
    global currentPosition

    if (sentence[currentPosition] == 'IfSym'):
        currentPosition+=1
        if (sentence[currentPosition] == 'LbrakSym'):
            currentPosition+=1
            compound_statement(sentence)
            if (sentence[currentPosition] == 'RCurlSym'):
                currentPosition+=1
                return True
            else:
                terminate(False, sentence[currentPosition])
        else:
            terminate(False, sentence[currentPosition])
    else:
        terminate(False, sentence[currentPosition])


def end_prog(sentence):
    global currentPosition
    print("endprog")
    if (sentence[currentPosition] == 'SystemSym'):
        currentPosition+=1
        if (sentence[currentPosition] == 'PeriodSym'):
            currentPosition+=1
            if (sentence[currentPosition] == 'ExitSym'):
                currentPosition+=1
                if (sentence[currentPosition] == 'LparenSym'):
                    currentPosition+=1
                    if (sentence[currentPosition] == 'IdentSym'):
                        currentPosition+=1
                        if (sentence[currentPosition] == 'RparenSym'):
                            currentPosition+=1
                            if (sentence[currentPosition] == 'SemicolonSym'):
                                currentPosition+=1
                                CG.genProgExit()
                                print("gen prog exit complete")
                                CG.genProgram()
                                #terminate(True, sentence)
                                method_body(sentence)
                            else:
                                terminate(False, sentence[currentPosition])
                        else:
                            terminate(False, sentence[currentPosition])
                    else:
                        terminate(False, sentence[currentPosition])
                else:
                    terminate(False, sentence[currentPosition])
            else:
                terminate(False, sentence[currentPosition])
        else:
            terminate(False, sentence[currentPosition])
    else:
        terminate(False, sentence[currentPosition])
        
def identifier():
    print("incomplete")

def terminate(res, current):
    global currentPosition

    if res:
        # sys.stdout.write("accepted: %s " % current);
        print("gen prog exit begin")
    else:
        sys.stdout.write("rejected: %s " % current);
        sys.exit();
   
if __name__ == "__main__": main()
