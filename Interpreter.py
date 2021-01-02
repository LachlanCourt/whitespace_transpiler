import sys
print('Reading from text file...')
code = []
file = open("code.txt", "r")
for i in file:
    for j in i:
        if ord(j) in [32, 9, 10]:
            code.append(ord(j))
file.close()
FINAL_CODE_LENGTH = len(code)


codeOutput = ["import sys", "heap = {}", "stack = []"]

## Instruction Modification Parameters
def stackManipulation():
    if len(code) > 0:
        if code[0] == 32:
            del(code[0])
            convertNumber()
            return
        elif len(code) > 1 and code[0] == 10 and code[1] == 32:
            del(code[0])
            del(code[0])
            codeOutput.append("stack.append(stack[len(stack) - 1])")
            return
        elif len(code) > 1 and code[0] == 10 and code[1] == 9:
            del(code[0])
            del(code[0])

            codeOutput.append("temp = stack[len(stack) - 1]")
            codeOutput.append("stack[len(stack) - 1] = stack[len(stack) - 2]")
            codeOutput.append("stack[len(stack) - 2] = temp")
            return
        elif len(code) > 1 and code[0] == 10 and code[1] == 10:
            del(code[0])
            del(code[0])

            codeOutput.append("del(stack[len(stack) - 1])")
            return
    else:
        parsingError()

def arithmetic():
    pass

def heapAccess():
    pass

def flowControl():
    pass

def inputOutput():
    pass

#Internal functions
def parsingError():
    print("Error parsing code at position " + str(FINAL_CODE_LENGTH - len(code)) + ". Please check input and try again")
    sys.exit()

def binaryToInt(binary):
    output = 0
    additionValue = 1
    newInput = ''
    for i in range(len(binary)):
        newInput += binary[len(binary) - 1 - i]
    for i in range(len(newInput)):
        if newInput[i] == '1':
            output += additionValue
        additionValue *= 2
    return output

def convertNumber():
    #First character of the number indicates whether it is positive or negative
    if len(code) < 1: #Check twice, for the sign and for the LineFeed token
        parsingError()
    sign = 0
    if code[0] == 32:
        sign = 1
    elif code[0] == 9:
        sign = -1
    else:
        parsingError()
    del(code[0])

    number = ""
    while len(code) > 1 and code[0] != 10:# A LineFeed indicates the end of the number
        if code[0] == 32:
            number += "0"
        if code[0] == 9:
            number += "1"
        del(code[0])
    #Delete the LineFeed token
    if len(code) == 0:
        parsingError()
    del(code[0])

    codeOutput.append("stack.append(" + str((sign* binaryToInt(number))) + ")")

while len(code) > 0:
    #Determine Instruction Modification Parameter
    if code[0] == 32:
        del(code[0])
        stackManipulation()
    elif len(code) > 1 and code[0] == 9 and code[1] == 32:
        del(code[0])
        del(code[0])
        arithmetic()
    elif len(code) > 1 and code[0] == 9 and code[1] == 9:
        del(code[0])
        del(code[0])
        heapAccess()
    elif code[0] == 10:
        del(code[0])
        flowControl()
    elif len(code) > 1 and code[0] == 9 and code[1] == 10:
        del(code[0])
        del(code[0])
        inputOutput()
    else:
        parsingError();


print('Code output:\n\n')
for i in codeOutput:
    print(i)


    
