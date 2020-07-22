import random
from insertion_sort import *

if __name__ == "__main__":
  A = [random.randint(0, 100) for i in range(10)]
  print(A)
  B = insertion_sort(A)
  print(B)