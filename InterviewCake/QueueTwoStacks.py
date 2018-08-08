
in_stack = []
out_stack = []

def enqueue(item):
    in_stack.append(item)

def dequeue():
    if len(out_stack) == 0:

        # Move items from in_stack to out_stack, reversing order
        while len(in_stack) > 0:
            newest_in_stack_item = in_stack.pop()
            out_stack.append(newest_in_stack_item)

            # If out_stack is still empty, raise an error
        if len(out_stack) == 0:
            raise IndexError("Can't dequeue from empty queue!")

    return out_stack.pop()


enqueue(10)
print in_stack
print out_stack
enqueue(12)
print in_stack
print out_stack
enqueue(13)
print in_stack
print out_stack
enqueue(14)
print in_stack
print out_stack
print dequeue()
print in_stack
print out_stack
print dequeue()
print in_stack
print out_stack
enqueue(15)
print in_stack
print out_stack
print dequeue()
print in_stack
print out_stack
