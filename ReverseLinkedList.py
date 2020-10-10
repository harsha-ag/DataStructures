def reverseList(self, head):
    if head==None:
        return 0
    if head.next==None:
        return head
    n=None
    curr=head
    while(cur.next!=None):
        temp=curr.next
        curr.next=n
        n=curr
        curr=temp
    head=curr
    return head


    #A>B>C>D
#N<A<B<C<D