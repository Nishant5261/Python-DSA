from sll import *
ll=Sll()
ll.append(1)
ll.append(12)
ll.append(13)
ll.append(14)
ll.append(15)
z=ll.tail
ll.append(16)
ll.append(17)
ll.append(18)
ll.append(19)
#ll.tail.next=z
f=ll.head
cy=False
s=ll.head
while f!=None and f.next!=None:
    s=s.next
    f=f.next.next
    if f==s:
        cy=True
        break
    
print(cy)
    
