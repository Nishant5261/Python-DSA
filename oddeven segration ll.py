from sll import *
ll=Sll()
ll.append(8)
ll.append(4)
ll.append(3)
ll.append(2)
ll.append(18)
ll.append(9)
ll.append(1)
ll.traversal()
odd=ll.head
even=ll.head.next
e_he=ll.head.next
if odd is None and odd.next is None:
    pass
while even!= None and even.next!=None:
    odd.next=even.next
    odd=even.next
    even.next=odd.next
    even=even.next
odd.next=e_he
print() 
ll.traversal()
