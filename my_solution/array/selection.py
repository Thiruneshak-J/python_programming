n=int(input("enter the size of list:"))
n=list(int(input("enter the number:")) for _ in range(n))
for i in range(0,len(n)):
    s=i
    for j in range(i+1,len(n)):
        if n[j]<n[s]:
            s=j
    n[i],n[s]=n[s],n[i]
print(n)
        