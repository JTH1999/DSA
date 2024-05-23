class Node: 
    def __init__(self, value, next = None, prev = None):
        self.value = value
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def prepend(self, item):
        length += 1

        node = Node(item)
        if self.head is None:
            self.head, self.tail = node
            return

        self.head.prev = node
        self.head = node


    def insertAt(self, item, index):
        if index > length:
            raise Exception("index can't be greater than length")
        elif index == length:
            self.append(item)
            return
        elif index == 0:
            self.prepend(item)
            return

        length += 1

        current = self.head
        for i in range(index):
            current = current.next

        node = Node(item)
        prev = current.prev
        node.next = current
        node.prev = prev
        prev.next = node
        current.prev = node

    def append(self, item):
        self.length += 1

        node = Node(item)

        if self.head is None:
            self.head, self.tail = node
            return
        
        self.tail.next = node
        node.prev = self.tail
        self.tail = node

    def remove(self, item):
        current = self.head
        for i in range(self.length):
            if current.value == item:
                break
            current = current.next
        
        if current is None:
            return None

        return self.removeNode(current)

    def removeAt(self, index):
        node = self.getAt(index)
        if node is None:
            return None

        return self.removeNode(node)

    def get(self, index):
        return self.getAt(index).value

    def getAt(self, index):
        current = self.head
        for i in range(index):
            current = current.next
        
        return current

    def removeNode(self, node):
        self.length -= 1
        if self.length == 0:
            out = self.head.value
            self.head, self.tail = None
            return out

        
        prev = node.prev
        next = node.next

        if prev:
            prev.next = next
        else: # current is head
            next.prev = None
            self.head = next

        if next:
            next.prev = prev
        else: # current is tail
            prev.next = None
            self.tail = prev

 
    


