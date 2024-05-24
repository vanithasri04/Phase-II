class Treenode:
    def __init__(self,data=0,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
def printlevelorder(root):
    result=[]
    queue=[root]
    while(len(queue)>0):
        result.append(queue[0].data)
        node=queue.pop(0)
        if(node.left):
            queue.append(node.left)
        if(node.right):
            queue.append(node.right)
    print(result)
def insertIntoOBS(root,val):
    if not root:
        return Treenode(val)
    if root.data>val:
        root.left=insertIntoOBS(root.left,val)
    else:
        root.right=insertIntoOBS(root.right,val)
    return root

# obj1=Treenode(10)
# obj2=Treenode(20)
# obj3=Treenode(30)
# obj2.left=obj1
# obj2.right=obj3
root=None
l=[20,30,10,40,50]
for i in l:
    root=insertIntoOBS(root,i)
printlevelorder(root)

    