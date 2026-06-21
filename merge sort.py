def merge(a,b):
    i=0
    j=0
    x=len(a)
    y=len(b)
    ts=[]
    while i<x and j<y:
        if a[i]<b[j]:
            ts.append(a[i])
            i+=1
        else:
            ts.append(b[j])
            j+=1
    if i<x:
        while i<x:
            ts.append(a[i])
            i+=1
    if j<y:
        while j<y:
            ts.append(b[j])
            j+=1
        
    return ts

def divide(ar):
    if len(ar)==1:
        return ar
    l=len(ar)//2
    left=ar[0:l]
    right=ar[l:len(ar)]
    l_s=divide(left)
    r_s=divide(right)
    s=merge(l_s,r_s)
    return s

arr=[2,4,1,3,7,1,3,2 ,5,6]
h=divide(arr)
print(h)
