class MinHeap:
    def __init__(self):
        self.length = 0
        self.data = []

    def insert(self, value):
        # logn time
        self.data[self.length] = value
        self._heapifyUp(self.length)
        self.length += 1

    def delete(self) -> int:
        # logn time
        if self.length == 0:
            return -1
        
        out = self.data[0]
        self.length -= 1
        if self.length == 0:
            self.data = []
            return out
        
        self.data[0] = self.data[self.length]
        self._heapifyDown(0)
        return out

    def _parent(index):
        return (index - 1) // 2
    
    def _leftChild(index):
        return index * 2 + 1
    
    def _rightChild(index):
        return index * 2 + 2
    
    def _heapifyUp(self, index):
        if index == 0:
            return

        parentIndex = self._parent(index)
        parentValue = self.data[parentIndex]
        value = self.data[index]

        if parentValue <= value:
            return
        
        self.data[parentIndex] = value
        self.data[index] = parentValue

        return self._heapifyUp(parentIndex)
    
    def _heapifyDown(self, index):
        leftIndex = self._leftChild(index)
        rightIndex = self._rightChild(index)

        if index >= self.length or leftIndex >= self.length:
            return
        
        value = self.data[index]
        leftValue = self.data[leftIndex]
        if rightIndex < self.length:
            rightValue = self.data[rightIndex]
        
        if rightValue and rightValue < leftValue: 
            minIndex = rightIndex
            minValue = rightValue
        else:
            minIndex = leftIndex
            minValue = leftValue

        if value > minValue:
            self.data[index] = minValue
            self.data[minIndex] = value
            self._heapifyDown(minIndex)

     
        
        


