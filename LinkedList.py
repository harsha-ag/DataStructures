#LinkedList
class Node:
    def __init__(self,value,NextNode=None):
        self.value=value
        self.NextNode=NextNode
class LinkedList:
    def __init__(self, head=None):
        self.head=head
    def insert(self,value):
        node=Node(value)
        if self.head is None:
            self.head=node
            return
        currentNode=self.head
        while True:
            if currentNode.NextNode is None:
                currentNode.NextNode = node
                break
                currentNode=currentNode.NextNode
    def printLL(self):
        currentNode=self.head
        while currentNode is not None:
            print(currentNode.value)
            currentNode=currentNode.NextNode
        print('None')

    def beginingList(self,value):
        node=Node(value)
        if self.head is None:
            self.head=node
        else:
            node.NextNode=self.head
            self.head=node

    def midInsert(self,value,position):
        c=0
        node=Node(value)
        if self.head is None:
            self.head=node
        else:
            cur=self.head
            while cur.NextNode is not None:
                c+=1
                if c==position-1:
                    node.NextNode=cur.NextNode
                    cur.NextNode=node
                break
    def deleteLL(self):
        temp=self.head
        if temp is not None:
            self.head=temp.NextNode
            temp=None
            return






#Node1=Node("3")
#Node2=Node("7")
#Node3=Node("10")
#Node4=Node("11")
'''
Node1.NextNode=Node2
Node2.NextNode=Node3
Node3.NextNode=Node4

currentNode=Node1
while True:
    print (currentNode.value)
    if currentNode.NextNode is not None:
        currentNode=currentNode.NextNode
    else:
        print("None")
        break
'''
print(len("Hello"))
ll=LinkedList()
ll.insert("0")
ll.insert("9")
ll.printLL()
ll.beginingList("8")
ll.midInsert("4",2)
ll.printLL()
ll.deleteLL()
ll.printLL()