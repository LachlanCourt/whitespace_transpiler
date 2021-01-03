import sys
heap = {}
stack = []
stack.append(7)
stack.append(3)
stack[len(stack) - 2] = stack[len(stack) - 2] % stack[len(stack) - 1]
del(stack[len(stack) - 1])

print(stack)
