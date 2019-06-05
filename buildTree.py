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
        #print(rootn)
        infoRoot(rootn)
        return rootn

# Show informations about the tree and return the tree
def infoRoot(rootn):
    tree = rootn
    print(tree)
    nLeaves = tree.leaf_count
    #leaves = tree.leaves
    maxNode = tree.max_node_value
    treeHeight = tree.height 

    print(" >> General information about your binary tree: ")
    print('Max node value: ', maxNode)
    print('Number of leaves: ', nLeaves)
    #print('Leaves: ', leaves)
    print('Tree height: ', treeHeight)
    code1(tree)
    return tree

#Function return all leaves indexes of tree as a vector
def code1(tree):
    tree = tree
    nNodes = tree.size
    nodes = list(range(nNodes))
    a = nodes.pop()
    vector = list(filter(lambda x: (x%2 != 0), nodes))
    vector.append(a)
    code2(vector, tree)
    return vector, tree

def code2(vector,tree):
    vectorCode = [0]
    vectorTree = vector
    for i in range(len(vectorTree)-1):
        vectorCode[i] = vectorCode[i-1] * 2 + 2
        vectorCode.append(0)
    a = vectorCode.pop()
    vectorCode.insert(0,a)
    print(vectorCode)
    return vectorCode

      

        




 