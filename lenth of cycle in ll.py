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
ll.append(21)
ll.append(28)
ll.append(31)
ll.append(19)
ll.tail.next=z
ll.traversal()
f=ll.head
cy=0
s=ll.head
l=0
sl=0
while f!=None and f.next!=None:
    s=s.next
    f=f.next.next
    l+=1
    if f==s:
        s=ll.head
        while f!=s:            
            s=s.next
            f=f.next
        print()
        print(f.val)
        break
print(l) 


    
