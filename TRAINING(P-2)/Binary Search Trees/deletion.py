class TreeNode:
    def __init__(self, val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
def insertIntoBST(root,val):
    if root==None:
        return TreeNode(val)
    elif(root.val>val):
        root.left=insertIntoBST(root.left,val)
    else:
        root.right=insertIntoBST(root.right,val)
    return root
def printbst(root):
    Q=[root]
    result=[]
    while(Q):
        result.append(Q[0].val)
        node=Q.pop(0)
        if(node.left):
            Q.append(node.left)
        if(node.right):
            Q.append(node.right)
    print(result)
def findInorderPredessor(root):
    while root.left != None:
        root = root.left 
    return root.data
 
def deleteInBST(root, val):
    if root == None:
        return None 
    elif root.data > val:
        root.left = deleteInBST(root.left, val)
    elif root.data < val:
        root.right = deleteInBST(root.right, val)
    else:
        if root.left == None and root.right == None:
            return None 
        elif root.left == None:
            return root.right 
        elif root.right == None:
            return root.left 
        else:
            predessor = findInorderPredessor(root)
            root.data = predessor 
            root.right = deleteInBST(root.right, predessor)
        return root
def findInorderSuccessor(root):
    while root.left != None:
        root = root.left 
    return root.val
 
def deleteNode(root, val) :
    if root == None:
        return None 
    elif root.val > val:
        root.left = deleteNode(root.left, val)
    elif root.val < val:
        root.right = deleteNode(root.right, val)
    else:
        if root.left == None and root.right == None:
            return None 
        elif root.left == None:
            return root.right 
        elif root.right == None:
            return root.left 
        else:
            successor = findInorderSuccessor(root.right)
            root.val = successor 
            root.right = deleteNode(root.right, successor)
    return root
            
root=None
l=[10,20,3,4,5,60]
for i in l:
    root=insertIntoBST(root,i)
printbst(root)
deleteNode(root,4)
printbst(root)