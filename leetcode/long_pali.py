s=input("enter the string:")
out=[]
for i in range(len(s)):
    seen=[]
    for j in range(i,len(s)):
        if