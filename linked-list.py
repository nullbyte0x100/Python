class Node:
    def __init__(self,data=None):
        self.data = data
        self.next=None
class Linked:
    def __init_(self):
        self.head=None
    def printList(self):
        value=self.head
        while value is not None:
            print(value.data)
            value=value.next
    # insert at beginning
    def atBeginning(self,beginningData):
        beginningNode=Node(beginningData)
        beginningNode.next=self.head
        self.head=beginningNode
    # insert at the end
    def  atEnd(self,endData):
        endNode=Node(endData)
        if self.head is None:
            self.head=endNode
            return
        lastValue=self.head
        while (lastValue.next):
            lastValue.next=endNode
        lastValue.next=endNode
l=Linked()
l.head=Node("Monday")
day_2=Node("Tuesday")
day_3=Node("Wednesday")
l.head.next=day_2
day_2.next=day_3
day_3.next=None
l.atBeginning("Days of the week")
l.atEnd("Thursday")
l.printList()