n=[6,25,50,70,14,74,67,1]
for i in range(0,len(n)):
    for j in range(0,len(n)-1-i):
        s=False
        if n[j]>n[j+1]:
            n[j],n[j+1]=n[j+1],n[j]
            s=True
    if not s:
        break
print(n)
