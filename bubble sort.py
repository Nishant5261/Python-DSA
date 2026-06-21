def bubble(a):
    n=len(a)
    c=0
    while c<n-1:
        for i in range(n-1):
            if a[i]>a[i+1]:
                a[i],a[i+1]=a[i+1],a[i]
        c+=1
        n-=1
a=[2,3,1,4,6,5]
bubble(a)
print(a)
        
