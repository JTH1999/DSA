# DEPTH FIRST TREE TRAVERSALS

# Pre order

def preOrderWalk(current, path):
    if not current:
        return
    
    #pre 
    path.push(current.value)

    #recurse
    preOrderWalk(current.left, path)
    preOrderWalk(current.right, path)

    # post 
    return path

def preOrderSearch(head):
    return preOrderWalk(head, [])

# In order

def inOrderWalk(current, path):
    if not current:
        return

    #recurse
    inOrderWalk(current.left, path)
    path.push(current.value)
    inOrderWalk(current.right, path)

    # post 
    return path

def inOrderSearch(head):
    return inOrderWalk(head, [])

# Post order

def postOrderWalk(current, path):
    if not current:
        return
    
    #recurse
    postOrderWalk(current.left, path)
    postOrderWalk(current.right, path)
    
    # post 
    path.push(current.value)
    return path

def postOrderSearch(head):
    return postOrderWalk(head, [])