s1=input("enter forst string :  ")
s2=input("enter second string :  ")
s1=s1.replace(" ","").upper()
s2=s2.replace(" ","").upper()
if sorted(s1) == sorted(s2):
    print("ANAGRAMS")
else:
    print("NOPE")
