def bb(n):
    for i in range(0,len(n)-1):
        for j in range(i+1,len(n)):
            if n[i]>n[j]:
                temp=n[i]
                n[i]=n[j]
                n[j]=temp
    return n
n=list(map(int,input("enter the numbers:").split(",")))
out=bb(n)
print("sorted list is",out)
