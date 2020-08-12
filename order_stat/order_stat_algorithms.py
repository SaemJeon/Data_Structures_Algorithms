import random
import copy
from randomized_select import *

if __name__ == "__main__":
  arr = [random.randint(0, 100) for i in range(10)]
  print(arr)
  print(randonmized_select(copy.deepcopy(arr), 0, len(arr) - 1, 6))