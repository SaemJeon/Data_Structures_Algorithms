import random

def randonmized_select(arr, low, high, i):
  if low == high:
    return arr[low]
  q = randomized_partition(arr, low, high)
  k = q - low + 1
  if i == k:
    return arr[q]
  elif i < k:
    return randonmized_select(arr, low, q-1, i)
  else:
    return randonmized_select(arr, q+1, high, i-k)

def partition(arr, low, high):
  x = arr[high]
  i = low - 1
  for j in range(low, high):
    if arr[j] <= x:
      i += 1
      arr[i], arr[j] = arr[j], arr[i]
  arr[i+1], arr[high] = arr[high], arr[i+1]
  return i+1

def randomized_partition(arr, low, high):
  i = random.randint(low, high)
  arr[i], arr[high] = arr[high], arr[i]
  return partition(arr, low, high)