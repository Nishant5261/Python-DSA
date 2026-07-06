from dll import *
dl=Dll()
dl.append(1)
dl.append(1)
dl.append(1)
dl.append(1)
dl.append(6)
dl.append(6)
dl.append(10)
dl.append(10)
dl.traverse()
cur=dl.head
while cur.next!=None :
    if cur.val==cur.next.val:
        temp=cur.next
        if cur.next.next:
            cur.next.next.prev=cur
            cur.next=cur.next.next
        else:
            cur.next=cur.next.next
            del temp
            break
        del temp
    else:
        cur=cur.next
dl.traverse()
            
