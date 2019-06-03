from binarytree import  Node

def firstRound(vector):
    a = vector.pop()
    b = vector.pop()
    vector.append(a+b)
    firstRoot = Node(a+b)
    firstRoot.left = Node(b)
    firstRoot.right= Node(a)
    nRound(vector, firstRoot)
    return [vector, firstRoot]

def nRound(vector, root):
    tempRoot = root
    a = vector.pop()
    b = vector.pop()
    if  (a+b)  < 1.0:
        vector.append(a+b)
        rootn = Node(a+b)
        rootn.right = tempRoot
        rootn.left = Node(b)
        return nRound(vector, rootn)   
    else:    
        rootn = Node(a+b)
        rootn.right = tempRoot
        rootn.left = Node(b) 
        print(rootn)
        return rootn








 