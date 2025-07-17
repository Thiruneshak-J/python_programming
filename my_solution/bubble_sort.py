n=[86,25,50,70,14,74,67,1]
print("unsorted",n)
for i in range(0,len(n)-1):
    s=False
    for j in range(0,len(n)-1-i):
        if n[j]>n[j+1]:
            n[j],n[j+1]=n[j+1],n[j]
            s=True
    if not s:
        break
print(n)