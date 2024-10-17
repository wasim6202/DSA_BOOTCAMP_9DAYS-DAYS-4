class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
    
    def is_empty(self):
        return self.top is None
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(f"Pushed {data} to the stack")
    
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        popped = self.top.data
        self.top = self.top.next
        return popped
    
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.top.data
    
    def display(self):
        if self.is_empty():
            print("Stack is empty")
            return
        temp = self.top
        print("Stack (top to bottom):", end=" ")
        while temp:
            print(temp.data, end=" -> " if temp.next else "")
            temp = temp.next
        print()

# Test the Stack
if __name__ == "__main__":
    stack = Stack()

    # Push elements
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    # Display the stack
    stack.display()

    # Pop an element
    print("Popped:", stack.pop())
    stack.display()

    # Peek at the top element
    print("Top element:", stack.peek())

    # Pop until empty
    print("Popping all elements:")
    while not stack.is_empty():
        print("Popped:", stack.pop())

    # Try to pop from empty stack
    print(stack.pop())

    # Push more elements
    stack.push(5)
    stack.push(6)
    stack.display()