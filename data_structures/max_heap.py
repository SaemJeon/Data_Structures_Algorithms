class MaxHeap:
  def __init__(self):
    self.size = 0
    self.heap = []

  def parent(self, pos):
    return pos // 2
  
  def left(self, pos):
    return 2 * pos

  def right(self, pos):
    return 2 * pos + 1
    
  def exchange(self, pos1, pos2):
    self.heap[pos1], self.heap[pos2] = self.heap[pos2], self.heap[pos1]

  def heapify(self, pos):
    if (2 * pos < self.size) and (self.heap[2 * pos] > self.heap[pos]):
      largest = 2 * pos
    else:
      largest = pos
    
    if (2 * pos + 1 < self.size) and (self.heap[2 * pos + 1] > self.heap[largest]):
      largest = 2 * pos + 1

    if largest != pos:
      self.exchange(pos, largest)
      self.heapify(largest)

  def insert(self, new):
    self.heap.append(new)
    self.size += 1
    current = self.size - 1
    while self.heap[self.parent(current)] < self.heap[current]:
      self.exchange(current, self.parent(current))
      current = self.parent(current)

  def buildHeap(self, arr):
    self.heap = arr
    self.size = len(arr)
    for i in range(len(self.heap)//2, -1, -1):
      self.heapify(i)

  def extractMax(self):
    largest = self.heap[0]
    self.heap[0] = self.heap[self.size - 1]
    self.heap.pop()
    self.size -= 1
    self.heapify(0)
    return largest


newHeap = MaxHeap()
newHeap.buildHeap([4, 1, 3, 2, 16, 9, 10, 14, 8, 7])
print(newHeap.extractMax())
print(newHeap.heap)
print(newHeap.extractMax())
print(newHeap.heap)