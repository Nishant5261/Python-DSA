def part(a,l,h):
    p=a[l]
    i,j=l,h
    while i<j:
        while a[i]<=p and i< h :
            i+=1
        while a[j]>=p and j>l :
            j-=1
        if i<j:
            a[i],a[j]=a[j],a[i]
    a[j],a[l]=a[l],a[j]
    return j
def quick(arr,l,h):
    if l<h:
        n=part(arr,l,h)
        quick(arr,l,n-1)
        quick(arr,n+1,h)    
     
arr=[4,6,1,7,2,5,3]
quick(arr,0,len(arr)-1)
print(arr)
    
    
