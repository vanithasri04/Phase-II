class Box:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

def printlevelorder(root):
    result=[]
    queue=[]
    queue.append(root)
    while(len(queue)>0):
        result.append(queue[0].data)
        node=queue.pop(0)
        if(node.left):
            queue.append(node.left)
        if(node.right):
            queue.append(node.right)
    return result
obj1=Box(10)
obj2=Box(20)
obj3=Box(30)
obj4=Box(40)
obj5=Box(50)
obj2.left=obj1
obj2.right=obj3
obj1.left=obj4
obj1.right=obj5
print(printlevelorder(obj2))