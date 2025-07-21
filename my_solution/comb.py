'''n=int(input("enter the objects:"))
r=int(input("enter the combinations to check:"))
r1=n-r
n_fact=1
r_fact=1
r1_fact=1
if r>n or n<0 or r<0:
    print(f"invalid output enter valid....")
else:
    for i in range(1,n+1):
        n_fact*=i
    for i in range(1,r+1):
        r_fact*=i
    for i in range(1,r1+1):
        r1_fact*=i
    ans=n_fact/(r_fact*r1_fact)
    print("the combinations is",ans)'''
def combi(n,r):
    n_f=1
    r_f=1
    r1=n-r
    r1_f=1
    if n<r or n<0 or r<0:
        print("invalid input")
    else:
        for i in range(1,n+1):
            n_f*=i
        for i in range(1,r+1):
            r_f*=i
        for i in range(1,r1+1):
            r1_f*=i
        ans=n_f/(r_f*r1_f)
        return ans
n=int(input("enter the objects:"))
r=int(input("enter the terms to combinations:"))
res=combi(n,r)
print(f"the combination for {n} and {r} is {res}")
        




