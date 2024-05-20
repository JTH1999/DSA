class Node: 
    def __init__(self, value, next = None, prev = None):
        self.value = value
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.length = 0
        self.head = undefined
        self.tail = undefined

    def prepend(item):
        length += 1

        node = Node(item)
        if self.head is None:
            self.head, self.tail = node
            return

        self.head.prev = node
        self.head = node


    def insertAt(item, index):
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

    def append(item):
        self.length += 1

        node = Node(item)

        if self.head is None:
            self.head, self.tail = node
            return
        
        self.tail.next = node
        node.prev = self.tail
        self.tail = node

    def remove(item):
        current = self.head
        for i in range(self.length):
            if current.value == item:
                break
            current = current.next
        
        if current is None:
            return undefined

        return self.removeNode(current)

    def removeAt(index):
        node = self.getAt(index)
        if node is None:
            return undefined

        return self.removeNode(node)

    def get(index):
        return self.getAt(index).value

    def getAt(index):
        current = self.head
        for i in range(index):
            current = current.next
        
        return current

    def removeNode(node):
        self.length -= 1
        if self.length == 0:
            out = self.head.value
            self.head, self.tail = None
            return out

        
        prev = current.prev
        next = current.next

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

 
    


