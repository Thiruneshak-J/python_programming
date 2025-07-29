n=list(str(input("enter the name:")))
n1=[]
for i in range(0,len(n)-1):
    for j in range(i+1,len(n)):
        if n[i]==n[j]:
            n1.append(n[j])
            break
print(n1)
            
