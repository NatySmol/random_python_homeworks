class Node:
    def __init__(self, value = 0, ):
        self.value = value
        self.next = None

class Seznam:
    def __init__(self):
        self.firstnode = None

    def prepend(self, value): #pripojovanni zepredu
        n = Node(value)
        n.next = self.firstnode
        self.firstnode = n
    def print(self):
        n = self.firstnode
        while n: #while n!=None
            print(n.value)
            n = n.next

s = Seznam()
for i in range(10):
    print(prepend.i)



