def merge_sort(A):
  if len(A) > 1:
    mid = len(A) // 2
    L = A[:mid]
    R = A[mid:]

    L = merge_sort(L)
    R = merge_sort(R)
    return merge(L, R)
  return A

def merge(s1, s2):
  s = []
  while s1 != [] and s2 != []:
    if s1[0] < s2[0]:
      s.append(s1.pop(0))
    else:
      s.append(s2.pop(0))
  
  while s1 != []:
    s.append(s1.pop(0))
  while s2 != []:
    s.append(s2.pop(0))

  return s