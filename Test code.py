import sys
heap = {}
stack = []
stack.append(42)
stack.append(stack[len(stack) - 1])
stack.append(17)
temp = stack[len(stack) - 1]
stack[len(stack) - 1] = stack[len(stack) - 2]
stack[len(stack) - 2] = temp
del(stack[len(stack) - 1])

print(stack)
