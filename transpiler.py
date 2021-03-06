import sys
print('Reading from text file...')
code = []
file = open("code.txt", "r")
for i in file:
    for j in i:
        if ord(j) in [32, 9, 10]:
            code.append(ord(j))
file.close()

# Used for error messages0
FINAL_CODE_LENGTH = len(code)


codeOutput = ["import sys", "heap = {}", "stack = []"]

# Instruction Modification Parameters
def stackManipulation():
    if len(code) > 0:
        if code[0] == 32:
            del(code[0])
            number = convertNumber()
            codeOutput.append("stack.append(" + number + ")")
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
    else:
        parsingError()

def arithmetic():
    if len(code) > 1:
        if code[0] == 32 and code[1] == 32:
            del(code[0])
            del(code[0])
            codeOutput.append("stack[len(stack) - 2] = stack[len(stack) - 2] + stack[len(stack) - 1]")
            codeOutput.append("del(stack[len(stack) - 1])")
        elif code[0] == 32 and code[1] == 9:
            del(code[0])
            del(code[0])
            codeOutput.append("stack[len(stack) - 2] = stack[len(stack) - 2] - stack[len(stack) - 1]")
            codeOutput.append("del(stack[len(stack) - 1])")
        elif code[0] == 32 and code[1] == 10:
            del(code[0])
            del(code[0])
            codeOutput.append("stack[len(stack) - 2] = stack[len(stack) - 2] * stack[len(stack) - 1]")
            codeOutput.append("del(stack[len(stack) - 1])")
        elif code[0] == 9 and code[1] == 32:
            del(code[0])
            del(code[0])
            codeOutput.append("stack[len(stack) - 2] = stack[len(stack) - 2] // stack[len(stack) - 1]")
            codeOutput.append("del(stack[len(stack) - 1])")
        elif code[0] == 9 and code[1] == 9:
            del(code[0])
            del(code[0])
            codeOutput.append("stack[len(stack) - 2] = stack[len(stack) - 2] % stack[len(stack) - 1]")
            codeOutput.append("del(stack[len(stack) - 1])")
        else:
            parsingError()
    else:
        parsingError()
    pass

def heapAccess():
    if code[0] == 32:# Store an item on the heap
        del(code[0])
        codeOutput.append("heap[stack[len(stack) - 2]] = stack[len(stack) - 1]")
        codeOutput.append("del(stack[len(stack) - 1])")
        codeOutput.append("del(stack[len(stack) - 1])")
    elif code[0] == 9:# Retrieve an item from the heap
        del(code[0])
        codeOutput.append("stack.append(heap[stack[len(stack) - 1]])")
        codeOutput.append("del(stack[len(stack) - 2])")
    else:
        parsingError()
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
        #Space is a 0, Tab is a 1, indicates a binary number
        if code[0] == 32:
            number += "0"
        if code[0] == 9:
            number += "1"
        del(code[0])
    #Delete the LineFeed token
    if len(code) == 0:
        parsingError()
    del(code[0])
    
    return str((sign * binaryToInt(number)))

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


    
