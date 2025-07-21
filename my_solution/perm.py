'''import math as m
n=int(input("enter the objects:"))
r=int(input("number of permutation:"))
ans=m.factorial(n)/m.factorial(n-r)
print(ans)
print(m.perm(3,2))
print(m.comb(3,2))'''

n=int(input("enter the objects:"))
r=int(input("number of permutation:"))
r1=n-r
temp=1
temp1=1
for i in range(1,n+1):
    a=temp*i
    temp=a
for i in range(1,r1+1):
    b=temp1*i
    temp1=b
ans=temp/temp1
print("the answer of permutation is",ans)

def per(n,r):
    n_f=1
    r1=n-r
    r1_f=1
    if n<r or n<0 or r<0:
        print("invalid input")
    else:
        for i in range(1,n+1):
            n_f*=i
        for i in range(1,r1+1):
            r1_f*=i
        ans = n_f/r1_f
        return ans
n=int(input("enter the objects:"))
r=int(input("enter the permutations terms:"))
res=per(n,r)
print(f"the permutations of given {n} and {r} is {res}")