def gcd(n):
    gcd=1
    for i in range(2,min(n)+1):
        if all(j%i==0 for j in n):
            gcd=i
    return gcd
n=list(map(int,input("enter the numbers by , :").split(",")))
res=gcd(n)
print("the gcd of numbers ",n,"are",res)

def gcd(a,b,c):
    gcd=1
    for i in range(2,min(a,b,c)+1):
        if a%i==0 and b%i==0 and c%i==0:
            gcd=i
    return gcd
a=int(input("enter the 1st number:"))
b=int(input("enter the 2nd number:"))
c=int(input("enter the 3rd number:"))

res=gcd(a,b,c)
print("the gcd of",a,",",b,"and",c,"is:",res)