class BinaryNode:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

# In a binary search tree, everything to left <= node and everything to right > node
class BinarySearchTree:
    def __init__(self, head):
        self.head = head
    
    def find(self, node, value):
        if not node:
            return False
        
        if node.value == value:
            return True

        if node.value < value:
            return self.find(node.right, value)

        return self.find(node.left, value)

        # Time complexity O(height) - somewhere between O(logn) for complete binary tree and O(n) for essentially linked list

    def insert(self, node, value):
        if node.value < value:
            if not node.right:
                node.right = BinaryNode(value)
                return
            else:
                return self.insert(node.right, value)
        else:
            if not node.left:
                node.left = BinaryNode(value)
                return
            else:
                return self.insert(node.left, value)

    # def delete(self, node, value):
        # case 1. no child -> delete
        # case 2. one child -> set parent to child
        # case 3. two children -> replace with either the smallest node on large side or largest on small side - make this decision based on the heights
        # we want to reorganise the highest as it should make it shorter