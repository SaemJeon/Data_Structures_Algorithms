import random
import copy
from insertion_sort import *
from merge_sort import *

if __name__ == "__main__":
  arr = [random.randint(0, 100) for i in range(10)]
  print(arr)
  print(insertion_sort(copy.deepcopy(arr)))
  print(arr)
  print(merge_sort(copy.deepcopy(arr)))