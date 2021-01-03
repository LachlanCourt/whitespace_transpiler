import sys
heap = {}
stack = []
stack.append(3)
stack.append(8)
print(stack)
print(heap)
heap[stack[len(stack) - 2]] = stack[len(stack) - 1]
del(stack[len(stack) - 1])
del(stack[len(stack) - 1])
print(stack)
print(heap)
stack.append(3)
stack.append(heap[stack[len(stack) - 1]])
del(stack[len(stack) - 2])

print(stack)
print(heap)
