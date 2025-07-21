n=list(map(int,input("enter the number:(by comma)").split(",")))
m=int(input("enter the times:"))
for i in range(0,m):
    temp=n[0]
    for i in range(0,len(n)-1):
        n[i]=n[i+1]
    n[len(n)-1]=temp
print(n)


    
