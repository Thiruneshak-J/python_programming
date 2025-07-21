import array as ar
n1=list(map(int,input("enter the number:").split(",")))
n=ar.array('i',n1)
x=int(input("enter the finding number:"))
count_v=0
for i in range(0,len(n)):
    if n[i]==x:
        count_v+=1
if count_v==0:
    count_v=-1
print(count_v)
