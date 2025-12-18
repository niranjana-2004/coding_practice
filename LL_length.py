class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insertAtEnd(self,data):
        newNode=Node(data)

        if self.head is None:
            self.head=newNode
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=newNode
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end='->')
            temp=temp.next
            print("None")
    def countNodes(self):
        temp=self.head
        count=0
        while temp:
            count+=1
            temp=temp.next
        return count
l=LinkedList()
l.insertAtEnd(10)
l.insertAtEnd(23)
l.insertAtEnd(40)
l.display()
print("no.of nodes",l.countNodes())