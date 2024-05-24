
class BOX:
    def __init__(self,data):
        self.data=data
        self.next=None
def printLinkedList(curr):
    while curr!=None:
        print(curr)
        print(curr.data)
        curr=curr.next
def insertAtTailNode(head,ele):
    temp=BOX(ele)
    if head==None:
        return temp
    tail=head
    while(tail.next!=None):
        tail=tail.next
    tail.next=temp
    return head
def insertAtBeggining(head,ele):
    temp=BOX(ele)
    if head==None:
        return temp
    temp.next=head
    return temp
head=None
obj1=BOX(10)
obj2=BOX(20)
obj3=BOX(30)
obj4=BOX(40)
obj1.next=obj2
obj2.next=obj3
obj3.next=obj4
obj4.next=None
print(insertAtTailNode(obj1,50))
printLinkedList(insertAtBeggining(obj1,34))