'''Input: List1: 5->6->3  // represents number 365
       List2: 8->4->2 //  represents number 248
Output: Resultant list: 3->1->6  // represents number 613

Input: List1: 7->5->9->4->6  // represents number 64957
       List2: 8->4 //  represents number 48
Output: Resultant list: 5->0->0->5->6  // represents number 65005'''
#creating nodes
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
#linkedlist class
class LinkedList:
    def __init__(self):
        self.head=None
    #creating newnodes and inserting into linkedlist
    def insert(self,newdata):
        newnode=Node(newdata)
        if self.head is None:
            self.head=newnode
            return
        lastnode=self.head
        while(lastnode.next is not None):
            lastnode=lastnode.next
        lastnode.next=newnode
    #function for printing linkedlist elements
    def printllist(self):
        currentnode=self.head
        if currentnode is None:
            print("linkedlist is empty")
            return
        while(currentnode is not None):
            print(currentnode.data)
            currentnode=currentnode.next
    #function for adding 2 numbers
    def add(self,head1,head2):
        current1=head1
        current2=head2
        carry=0
        while(current1 is not None or current2 is not None):
            
            if current1 is None:
                sum1=0
            else:
                sum1=current1.data
            if current2 is None:
                sum2=0
            else:
                sum2=current2.data
            sum=sum1+sum2+carry
            if sum<10:
                llistsum.insert(sum)
                carry=0
            else:
                sum=sum%10
                llistsum.insert(sum)
                carry=1
            if current1 is not None:
                current1=current1.next
            if current2 is not None:
                current2=current2.next
        if carry !=0:
            llistsum.insert(carry)
    #function for printing linkedlist elements in reverse order
    def print_rev(self,headnode):
        if headnode is None:
            return 
        self.print_rev(headnode.next)
        print(headnode.data)       
if __name__=="__main__":
    llist1=LinkedList()
    llist2=LinkedList()
    llistsum=LinkedList()
    llist1.insert(7)
    llist1.insert(5)
    llist1.insert(9)
    llist1.insert(4)
    llist1.insert(6)
    print("first number")
    llist1.print_rev(llist1.head)
    llist2.insert(8)
    llist2.insert(4)
    print("second number")
    llist2.print_rev(llist2.head)
    print("sum of first number and second number is")
    llist1.add(llist1.head,llist2.head)
    llistsum.print_rev(llistsum.head)
    







