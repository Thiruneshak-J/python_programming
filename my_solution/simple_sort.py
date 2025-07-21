n=[34,56,76,5,4,32,9]
print("the unsorted list\n",n)
for i in range(0,len(n)-1):
    for j in range(i+1,len(n)):
        if n[i]>n[j]:
            temp=n[i]
            n[i]=n[j]
            n[j]=temp
    print(n)     #every loop i output will print
#print(n) to print only last loop output which i=len(n-1)
                        

