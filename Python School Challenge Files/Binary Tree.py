string = input().split(" ")
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.value)
    def __repr__(self):
        return self.__str__()
tree = []
for i in string:
    tree.append(Node(None if i == "None" else int(i)))
def getTreeLength(node):
    treeContents = []
    treeSize = 0
    if Node.value == None:
        return 0
    
    if getTreeLength

