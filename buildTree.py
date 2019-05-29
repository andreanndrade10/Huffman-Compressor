from binarytree import tree, bst, heap, build, Node


def firstRound(vector):
    a = vector.pop()
    b = vector.pop()
    vector.append(a+b)
    firstRoot = Node(a+b, b, a)
    return vector, firstRoot



def nRound(vector, root):
    tempRoot = root
    a = vector.pop()
    b = vector.pop()

    if a+b < 1:
        vector.append(a+b)
        rootn = Node(a+b)
        rootn.right = tempRoot
        rootn.left = Node(b)
        nRound(vector, rootn)    
    rootn = Node(a+b)
    rootn.right = tempRoot
    rootn.left = Node(b)
    return rootn

root = Node(.2)
root.right = Node(.1)
root.left = Node(.1)
vector = [.3,.2,.2,.1,.2]
print(nRound(vector, root))



 