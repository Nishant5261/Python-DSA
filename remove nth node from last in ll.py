from sll import *
ll=Sll()
ll.append(3)
ll.append(18)
ll.append(8)
ll.append(16)
ll.append(31)
ll.append(21)
ll.append(12)
ll.traversal()
n=7
s=ll.head
f=ll.head
for i in range(n):
    f=f.next
if f==None:
    ll.head=s.next
else:
    while f.next!=None :
        s=s.next
        f=f.next
    s.next=s.next.next
print()
ll.traversal()
