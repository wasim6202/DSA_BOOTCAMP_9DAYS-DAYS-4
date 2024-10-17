class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        print(f"Enqueued: {data}")

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return data

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        current = self.front
        print("Queue:", end=" ")
        while current:
            print(current.data, end=" <- " if current.next else "")
            current = current.next
        print()

# Test Queue
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.display()
print("Dequeued:", queue.dequeue())
queue.display()
# Circular Queue using Linked List:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
            self.rear.next = self.front
        else:
            new_node.next = self.front
            self.rear.next = new_node
            self.rear = new_node
        print(f"Enqueued: {data}")

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        data = self.front.data
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.rear.next = self.front
        return data

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        current = self.front
        print("Circular Queue:", end=" ")
        while True:
            print(current.data, end=" <- ")
            current = current.next
            if current == self.front:
                break
        print()

# Test Circular Queue
cq = CircularQueue()
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.display()
print("Dequeued:", cq.dequeue())
cq.display()
cq.enqueue(4)
cq.display()

#Circular Queue using Linked List:
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Deque:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def add_front(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node
        print(f"Added to front: {data}")

    def add_rear(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node
        print(f"Added to rear: {data}")

    def remove_front(self):
        if self.is_empty():
            return "Deque is empty"
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        else:
            self.front.prev = None
        return data

    def remove_rear(self):
        if self.is_empty():
            return "Deque is empty"
        data = self.rear.data
        self.rear = self.rear.prev
        if self.rear is None:
            self.front = None
        else:
            self.rear.next = None
        return data

    def display(self):
        if self.is_empty():
            print("Deque is empty")
            return
        current = self.front
        print("Deque:", end=" ")
        while current:
            print(current.data, end=" <-> " if current.next else "")
            current = current.next
        print()

# Test Deque
deque = Deque()
deque.add_front(1)
deque.add_rear(2)
deque.add_front(3)
deque.add_rear(4)
deque.display()
print("Removed from front:", deque.remove_front())
print("Removed from rear:", deque.remove_rear())
deque.display()