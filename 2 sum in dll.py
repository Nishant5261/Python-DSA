from dll import *
dl=Dll()
dl.append(1)
dl.append(2)
dl.append(4)
dl.append(5)
dl.append(6)
dl.append(8)
dl.append(9)
dl.traverse()
t=7
res=[]
l=dl.head
r=dl.head
while r.next!=None:
    r=r.next

while l.val<r.val:
    if l.val+r.val>t:
        r=r.prev
    elif l.val+r.val<t:
        l=l.next
    else:
        te=[l.val,r.val]
        res.append(te)
        l=l.next
        r=r.prev    
        
    
print(res)
    
