from binarytree import build, Node


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
    if  a+b < 1.0:
        vector.append(a+b)
        rootn = Node(a+b)
        rootn.right = tempRoot
        rootn.left = Node(b)
        nRound(vector, rootn)
        #print(rootn)
    else:    
        rootn = Node(a+b)
        rootn.right = tempRoot
        rootn.left = Node(b) 
        print(rootn)   
        return rootn
    return rootn  
    
roota = Node(.2)
roota.right = Node(.1)
roota.left = Node(.1)
vectora = [.3,.2,.2,.1,.2]
print(nRound(vectora, roota))


 