import array as ar
n1=list(map(int,input("enter the numbers:").split(" ")))
n=ar.array('i',n1)
print("enterd numbers : ",n)
temp=0
for i in range(0,len(n)):
    temp+=n[i]
print(temp)
