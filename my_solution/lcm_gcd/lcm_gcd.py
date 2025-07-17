"""def gcd(n):
    gcd=1
    for i in range(2,min(n)+1):
        if all(j%i==0 for j in n):
            gcd=i
    return gcd
def lcm(n):
    res=gcd(n)
    pro=1
    for i in n:
        pro*=i
    lcm=pro//res
    return lcm
t=int(input("how many times do you want to calculate hcf and lcm:"))
for k in range(t):
    n=list(map(int,input("enter the numbers(seperated by space):").split(" ")))
    ch=input("enter the operations to perform GCD(g) or LCM(l):").lower()
    if ch=="g":
        res=gcd(n)
        print("the GCD of numbers is:",res)
    if ch=="l":
        res1=lcm(n)
        print("the LCM of these numbers is :",res1)"""
def gcd(a,b):
    gc=1
    for i in range(2,min(a,b)+1):
        if (a%i==0 and b%i==0):
            gc=i
    return gc
a=42
b=88
res=gcd(a,b)
print(res)


