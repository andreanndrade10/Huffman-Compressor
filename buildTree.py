from binarytree import tree, bst, heap, build, Node


def firstRound(vector):
    a = vector.pop()
    b = vector.pop()
    vector.append(a+b)
    firstRoot = Node(a+b, b, a)
    return vector, root



def nRound(vector, root):
    a = vector.pop()
    b = vector.pop()
    if a+b != 1:
        vector.append(a+b)
        rootn = Node(a+b)
        rootn.right = root
        rootn.left = Node(b)
        nRound(vector, rootn)
    return rootn
