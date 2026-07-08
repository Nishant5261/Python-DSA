from sll import Sll
ll=Sll()
ll.append(5)
ll.append(10)
ll.append(27)
ll.append(3)
ll.append(99)     
s=ll.head
f=ll.head
while f!=None and f.next!=None :
    s=s.next
    f=f.next.next
print(s.val)
    

