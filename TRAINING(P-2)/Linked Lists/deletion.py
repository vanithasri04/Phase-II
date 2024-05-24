class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def print_list(curr):
    while(curr!=None):
        print(curr.data,end=" -->")
        curr=curr.next
    print()
def insertatbegining(head,data):
    temp=Node(data)
    if head==None:
        return temp
    temp.next=head
    return temp
def insertionattail(head,data):
    temp=Node(data)
    if head==None:
        return temp
    tail=head
    while tail.next:
        tail=tail.next
    tail.next=temp
    return head
def deletionNode(head):
    curr=head
    if curr==None or curr.next==None:
        return None
    while curr.next.next:
        curr=curr.next
    curr.next=None
def deletionatbeginning(head):
    if head==None or head.next==None:
        return None
    temp=head.next
    head.next=None
    return temp
def deletionatspecificposition(head,position):
    if position==0:
        return deletionatspecificposition(head)
    currentIndex=0
    currentNode=head
    while currentIndex!=position-1:
        currentNode=currentNode.next
        currentIndex+=1
    temp=currentNode.next
    currentNode.next=currentNode.next.next
    temp.next=None
    return head
head=None
num=[10,20,30,40]
for i in num:
    head=insertionattail(head,i)
print_list(head)
#deletionatbeginning(head)
#head=deletionatbeginning(head)
deletionatspecificposition(head,3)
print_list(head)