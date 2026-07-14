s= input("enter the string")
step=2
while step<=len(s):
    for i in range(len(s)-step+1):
        sub=s[i:i+step]
        rev=sub[ : :-1]
        if sub==rev:
            print(sub)
    step+=1
