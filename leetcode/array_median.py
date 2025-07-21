import array as ar
num11=list(map(int,input()))
num1=ar.array('i',num11)
num22=list(map(int,input()))
num2=ar.array('i',num22)
num1.extend(num2)
for i in range(0,len(num1)):
    s=False
    for j in range(len(num1)-i-1):
        if num1[j]>num1[j+1]:
            num1[j],num1[j+1]=num1[j+1],num1[j]
            s=True
    if not s:
        break
l=len(num1)
if l%2==0:
    m=(num1[l//2-1] + num1[l//2])/2
else:
    m=float(num1[l//2])
print(m)



