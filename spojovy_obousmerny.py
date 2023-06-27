class Node:
    def __init__(self, value = 0, ):
        self.value = value
        self.next = None
        self.prev = None

class Seznam:
    def __init__(self):
        self.head = Node(None)
        self.head.next = self.head
        self.head.prev = self.head

    def is_empty(self):
        return self.head.next == self.head

    def prepend(self):
        n = Node(value)
        if self.is_empty():
            self.head.next = n
            self.head.prev = n
            n.prev = self.head
            n.next = self.head
        else: #seznam is not empty
            n.prev =self.head
            n.next = self.head.next
            self.head.next = n
            self.head.next.prev =n

    def append(self):
        if  self.is_empty():
            self.prepend(value)
        else:
            n = Node(value)
            n.next = self.head
            n. prev = self.head.prev
            self.head.prev = n
            n.prev.next = n
    def print(self):
        n = self.head.next
        while n != self.head:
            print(n.value)
            n = n.next


