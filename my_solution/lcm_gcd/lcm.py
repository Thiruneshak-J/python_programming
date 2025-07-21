#input format
def gcd(a,b):
    gcd=1
    for i  in range(2,min(a,b)+1):
        if a%i==0 and b%i==0:
            gcd=i
    return gcd
def lcm(a,b):
    res=gcd(a,b)
    lcm=a*b//res
    return lcm
a=int(input("enter the number:"))
b=int(input("enter the 2nd number:"))
res1=lcm(a,b)
print("lcm of numbers:",res1)

# list format
def gcd(n):
    gcd=1
    for i in range(2,min(n)+1):
        if all(j%i==0 for j in n):
            gcd=i
    return gcd
def lcm(n):
    res=gcd(n)
    pro=1
    for i in n :
        pro*=i
    lcm=pro//res
    return lcm
n=list(map(int,input("enter the list numbers(seperated by comma):").split(",")))
res1=lcm(n)
print("the LCM of numbers is:",res1)

