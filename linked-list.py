from tkinter.messagebox import NO


class Node:
    def __init__(self,data=None):
        self.data = data
        self.next=None
class Linked:
    def  __init__(self):
        self.head=None
    def  printList(self):
        value=self.head
        while value is not None:
            print(value.data)
            value=value.next
    def atBeginning(self,beginData):
        beginNode=Node(beginData)
        beginNode.next=self.head
        self.head=beginNode
l=Linked()
l.head=Node("Monday")
day_2=Node("Tuesday")
day_3=Node("Wednesday")
l.head.next=day_2
day_2.next=day_3
day_3.next=None
l.atBeginning("Days of the week")
l.printList()