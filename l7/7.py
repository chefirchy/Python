uniqueList = [5, 6, 7]
notUniqueList = [5, 6, 5]

def isListMembersUnique(ls: list):
  for li in ls:
    if(ls.count(li) != 1):
      return False
  return True

if isListMembersUnique(uniqueList):
  print(f'Элементы массива {uniqueList} - уникальны')
  

if not isListMembersUnique(notUniqueList):
  print(f'Элементы массива {notUniqueList} - не уникальны')