class Box:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def printInordertraversal(root):
    if root==None:
        return
    printInordertraversal(root.left)
    print(root.data,end=" ")
    printInordertraversal(root.right)

def printpreordertraversal(root):
    if root==None:
        return 
    print(root.data,end=" ")
    printpreordertraversal(root.left)
    printpreordertraversal(root.right)
def printpostordertraversal(root):
    if root==None:
        return
    printpostordertraversal(root.left)
    printpostordertraversal(root.right)
    print(root.data,end=" ")

obj1=Box(10)
obj2=Box(20)
obj3=Box(30)
obj4=Box(40)
obj5=Box(50)
obj2.left=obj1
obj2.right=obj3
obj1.left=obj4
obj1.right=obj5
printInordertraversal(obj2)
print()
printpreordertraversal(obj2)
print()
printpostordertraversal(obj2)
