#Doubly Linked List class definition
class DLL:
    def __init__(self,val=0,p=None,n=None):
        self.val = val
        self.prev = None
        self.next = None
class DLLN:

    def __init__(self,head=None):
        self.head=head

    def insert(self,val,pos=0):
        Node = DLL(val)
        if self.head is None:
            self.head = Node
            return
        if pos==1:
            Node.next = self.head
            self.head.prev = Node
            self.head=Node
        p = 0
        link = self.head
        while link.next!=None and p<pos:
            link=link.next
            p+=1
        Node.prev=link.prev
        link.prev.next = Node
        Node.next=link
        link.prev = Node
        #print(self.head.val)

    def deldll(self,pos=0):
        if self.head == None:
            print("Empty")
            return 0
        link = self.head
        if pos == 1:
            print(link.val)
            link.next=None
            self.head = self.head.next
            del link
            return 0
        p=0
        while p<pos and link.next!=None:
            link=link.next
            p+=1
        linkt=link.prev
        linkt.next=link.next.next
        if link.next:
            link.next.prev=linkt
            del link
            return 0




    def printdll(self):
        node = self.head
        if self.head is None:
            print("empty node")
            return 0
        while node!=None:
            print(str(node.val)+"->",end='')
            node=node.next
        if node==None:
            print("NULL")
        return 0

if __name__ == "__main__":
    dll=DLLN()
    dll.insert(2)
    dll.printdll()
    dll.insert(3,1)
    dll.printdll()
    dll.insert(1,2)
    dll.printdll()
    dll.deldll(1)
    dll.printdll()

