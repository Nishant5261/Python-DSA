from math import ceil,floor,sqrt
def isprime(num):
    for i in range(2,int(sqrt(num))+1):
        if num % i ==0:
            return False
    return True
def p_gen(req,l):
    n=1
    while req!=0:
        np1=(6*n)-1 if isprime((6*n)-1)== True else None
        np2=(6*n)+1 if isprime((6*n)+1)== True else None 
        n=n+1
        if np1== None:
            if np2== None:
                continue
            else:
                if req==1:
                    l.append(np2)
                    req=req-1
                else:
                    l.append(np2)
                    req=req-1
        else:
            if req==1:
                l.append(np1)
                req=req-1
            else:
                if np2== None:
                    l.append(np1)
                    req=req-1
                    
                else:
                    l.extend([np1,np2])
                    req=req-2

r1=int(input("enter no of prime number required :  " ))
p=[2,3]
req=r1-2
if req>0:
    p_gen(req,p)
for i in range(r1):
    print(p[i])

                 
