from dll import *
dl=Dll()
dl.append(10)
dl.append(12)
dl.append(10)
dl.append(2)
dl.append(5)
dl.traverse()
print(dl.head.val)
k=10
cur=dl.head
while cur.next!=None:
    if dl.head.val==k:
        dl.head.next.prev==dl.head.prev
        temp=dl.head
        dl.head=dl.head.next
        del temp
        cur=dl.head
        continue
    if cur.val==k:
        temp=cur.next
        cur.prev.next=cur.next
        cur.next.prev=cur.prev
        cur=temp
    else:
        cur=cur.next
dl.traverse()
print(dl.head.val)
    
