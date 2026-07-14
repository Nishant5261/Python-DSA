s=input("enter the string here : ")
spliter=input("enter the split key string here:  ") 
print(s)
try:
    z=s.split(spliter)
    print(z)
    recov=''
    for i in range(len(z)):
        if i==(len(z)-1) and z[i]=='':
            continue
        elif i==(len(z)-1):
            recov+=z[i]
        else:
            recov+=z[i]+spliter
    print(recov)
except ValueError:
    print("empty strings are non-breakable")

    
    
