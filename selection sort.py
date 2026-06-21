def sel(a):
    i=0
    r=len(a)
    while i<(r-1):
        min_ind=i
        for j in range(i+1,r):
            
            if a[j]<a[min_ind]:
                min_ind=j
        a[i],a[min_ind]=a[min_ind],a[i]
        i+=1
a=[3,1,4,6,2,5]
sel(a)
print(a)
