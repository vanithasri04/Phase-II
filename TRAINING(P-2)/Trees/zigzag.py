class Box:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
def Zigzag(root):
    if root==None:
        return
    queue=[root] #20
    result=[] 
   
    level=1
    while(len(queue)>0):
        n=len(queue) #1
        subresult=[]
        for i in range(n):
            currnode=queue.pop()
            subresult.append(currnode.data)
            if(currnode.left):
                queue.append(currnode.left)
            if(currnode.right):
                queue.append(currnode.right)
        if level%2==0:
            subresult=subresult[::-1]
        level+=1
        result.append(subresult)
    print(result)

        
obj1=Box(10)
obj2=Box(20)
obj3=Box(30)
obj4=Box(40)
obj5=Box(50)
obj2.left=obj1
obj2.right=obj3
obj1.left=obj4
obj1.right=obj5
Zigzag(obj2)