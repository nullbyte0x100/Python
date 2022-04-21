

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linked:
    def __init__(self):
        self.head=None
    def return_list(self):
        value=self.head
        while value is not None:
            print(value.data)
            value=value.next
    def atBegin(self,beginData):
        beginNode=Node(beginData)
        beginNode.next=self.head
        self.head=beginNode
    def atEnd(self,endData):
        endNode=Node(endData)
        if self.head is None:
            self.head=endNode
            return
        last=self.head
        while last.next:
            last=last.next
        last.next=endNode
    def atMiddle(self,midNode,midData):
        if midNode is None:
            print("Mentioned node is absent")
            return
        newMidNode=Node(midData)
        newMidNode.next=midNode.next
        midNode.next=newMidNode
    def removeNode(self,removeKey):
        headValue=self.head
        if headValue is not None:
            if headValue.data==removeKey:
                self.head=headValue.next
                headValue=None
                return
            while headValue is not None:
                if headValue.data==removeKey:
                    break
                previous=headValue
                headValue=headValue.next
            if headValue==None:
                return

            previous.next=headValue.next
            headValue=None
l=Linked()
l.head=Node("Monday")
day_2=Node("Tuesday")
day_3=Node("Wednesday")
day_4=Node("Thursday")
l.head.next=day_2
day_2.next=day_3
day_3.next=day_4
day_4.next=None
l.atBegin("Days of the week")
l.atEnd("Friday")
l.atMiddle(l.head.next.next.next,"At middle")
l.return_list()
print("+++++++++++++++++")
l.removeNode("Monday")
l.return_list()