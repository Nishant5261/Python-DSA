def ins(a):
    n=len(a)
    for i in range(1,n):        
        key=a[i]
        if key<a[i-1]:
            for j in range(i-1,-1,-1):
                if a[j]>key:
                    a[j+1]=a[j]
                    a[j]=key
a=[4,3,1,5,2,6]
ins(a)
print(a)
                    
        
    
