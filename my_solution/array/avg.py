import array as ar
n1=list(map(int,input("enter the number(seperated by comma:)").split(",")))
n=ar.array('i',n1)
temp=0
for i in range(0,len(n)):
    temp+=n[i]
avg=temp/len(n)
print("avg of array is :",avg)