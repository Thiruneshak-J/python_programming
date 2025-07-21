n=list(map(int,input("enter the elements:").split(" ")))
print("unsorted list",n)
for i in range(0,len(n)):
    m=i
    for j in range(i+1,len(n)):
        if n[m]>n[j]:
            m=j
    n[i],n[m]=n[m],n[i]
print(n)
