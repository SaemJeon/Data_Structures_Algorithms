# Worst case linear select algo
from randomized_select import *

def select(arr, low, high, i):
  groups = [[]] * ((high - low) // 5 + 1)

  for x in range(low, high+1):
    groups[(x - low) // 5] = groups[(x - low) // 5] + [arr[x]]
  
  medians = [sorted(l)[(len(l) - 1)//2] for l in groups]

  if len(medians) == 1:
    med = medians[0]
  else:
    med = select(medians, 0, len(medians) - 1, (len(medians) - 1)//2)

  # TODO: Add partiton logic here

select([1, 4, 6, 7, 2, 3, 8, 32, 11], 0, 8, 3)