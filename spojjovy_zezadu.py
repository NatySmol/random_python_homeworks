class Node:
    def __init__(self, value = 0, ):
        self.value = value
        self.next = None

class Seznam:
    def __init__(self):
        self.firstnode = None
        self.lastnode = None

    def append(self, value): #pripojovanni zepredu
        n = Node(value)
        if self.lastnode == None:
            self.lastnode = n
            self.firstnode = n
        else:
            self.lastnode.next = n

        self.lastnode.next = n
        self.lastnode = n

    def print(self):
        n = self.firstnode
        while n: #while n!=None
            print(n.value)
            n = n.next

s = Seznam()
for i in range(10):
    print(s.append(i))
s.print()
s.find(2)