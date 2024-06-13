stack = []
stack.append("a")
stack.append("b")
stack.append("c")
print(stack)
stack.pop()
print(stack)


def peek(st):
    return stack[-1]


def is_empty(st):
    return len(stack) == 0


print(peek(stack))
print(is_empty(stack))
