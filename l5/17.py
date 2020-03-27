#Файл для записи уже в папке с работами(Путь изначально кривой, ибо у меня немного НЕ так работает ОС)
from typing import List
# from os import write

FILE_TO_WRITE = 'C:\\Users\\chefi\\Documents\\file_to_write.txt'

class Tree:
  value: str
  children: list
  def __init__(self, value: str):
    self.value: str = value
    self.children: List[str] = []

  def append_child(self, value: str):
    assert(len(self.children) < 10)
    self.children.append(Tree(value))

  def setVal(self, value: str):
    self.value = value

def traverse_tree(tree: Tree, reducer: str='', separator="|> "):
  if(len(tree.children) == 0):
    file = open(FILE_TO_WRITE, 'a')
    file.write(reducer + tree.value + '\n')
    file.close()
  else:
    for sub_tree in tree.children:
      traverse_tree(sub_tree, reducer + tree.value + separator, separator)

def construct_tree() -> Tree:
  tree: Tree = Tree('0')
  for i in range(0, 10):
    tree.append_child(f"{i}")
    for j in range(0, 10):
      tree.children[i].append_child(f"{j}")
  return tree
  
tree = construct_tree()

traverse_tree(tree)

# print(tree.children[0].children[1].value)