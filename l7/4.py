arr1 = [22, 7, 6, 5]
arr2 = [11, 9, 2]

def reverseDescending(arr1, arr2):
  i = 0
  j = 0
  united = []
  while i < len(arr1) and j < len(arr2):
    if(arr1[i] > arr2[j]):
      united.append(arr1[i])
      i += 1
    else:
      united.append(arr2[j])
      j += 1
      
  if i < len(arr1) - 1:
    united += arr1[i:]

  else:
    united += arr2[j:]

  return united

united = reverseDescending(arr1, arr2)
print(united)