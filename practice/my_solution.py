#gcd----------------------- 1
'''a=int(input("enter the a number:"))
b=int(input("enter the b number:"))
c=int(input("enter the c number:"))
g=1
for i in range(2,min(a,b,c)+1):
    if a%i==0 and b%i==0 and c%i==0:
        g=i
print(g)'''
#gcd------------------------------ 1A
'''def gc(n):
    g=1
    for i in range(2,min(n)+1):
        if all(j%i==0 for j in n):
            g=i
    return g
n=list(map(int,input("enter the number by comma").split(",")))
res=gc(n)
print(res)'''
#lcm ---------------------------------- 2
'''n=list(map(int,input("enter the numbers (,)").split(",")))
g=1
for i in range(1,min(n)+1):
    if all(j%i==0 for j in n):
        g=i
pro=1
for j in range(0,len(n)):
    pro*=n[j]
lc=pro//g
print(lc)'''
#gcd _ lcm -------------------------2A
'''def gcd(n):
    g=1
    for i in range(1,min(n)+1):
        if all (j%i==0 for j in n):
            g=i
    return g
def lc(n):
    res=gcd(n)
    temp=1
    for j in range(0,len(n)):
            temp*=n[j]
    l=temp//res
    return l
n=list(map(int,input("enter the numbers(,)").split(",")))
ch=input("g or l").lower()
if ch=='g':
     res=gcd(n)
     print(res)
if ch=='l':
     res1=lc(n)
     print(res1)
'''
# area-------------------- 3
'''class circle:
    pi=3.14
    def __init__(self,rad):
        self.rad=rad
    def area(self):
        c=circle.pi*(self.rad**2)
        return c
r=int(input("radii:"))
c=circle(r)
print(c.area())
'''
'''# addind list ------------- 4
a=[1,2,3,4]
b=[6,7,8,9]
s=[]
for i in range(0,len(a)):
    d=a[i]+b[i]
    s.append(d)
print(*s)
# adding list (lambda)------------ 4A
a=[1,2,3,4]
b=[3,4,5,6]
x=list(map(lambda x,y:x+y,a,b))
print(x)
'''
#bubble sort------------------------5
'''n=list(map(int,input("enter the numbers:")))
print("unsorted list",n)
for i in range(0,len(n)-1):
    for j in range(i+1,len(n)):
        if n[i]>n[j]:
            temp=n[i]
            n[i]=n[j]
            n[j]=temp
print(n)
# func bubble ---------------- 5a
def bb(n):
    for i in range (0,len(n)-1):
        for j in range(i+1,len(n)):
            if n[i]>n[j]:
                temp=n[i]
                n[i]=n[j]
                n[j]=temp
    return n
n=list(map(int,input("enter the numbers:")))
res=bb(n)
print(res)'''
#comb------------------------ 6
'''n=int(input("enter the number:"))
r=int(input("enter the number:"))
a=n-r
n_f=1
r_f=1
a_f=1
for i in range(1,n+1):
    n_f*=i
for j in range(1,r+1):
    r_f*=j
for k in range(1,a+1):
    a_f*=k
ans=n_f//(r_f*a_f)
print(ans)
# comb--------------------- 6A
def co(n,r,a):
    n_f=1
    r_f=1
    a_f=1
    for i in range(1,n+1):
        n_f*=i
    for j in range(1,r+1):
        r_f*=j
    for k in range(1,a+1):
        a_f*=k
    ans=n_f//(r_f*a_f)
    return ans
n=int(input("enter the number:"))
r=int(input("enter the number:"))
a=n-r
res=co(n,r,a)
print(res)'''
#perm---------------------------7
'''n=int(input("enter the number:"))
r=int(input("enter the number:"))
a=n-r
def per(n,r,a):
    n_f=1
    r_f=1
    a_f=1
    for i in range(1,n+1):
        n_f*=i
    for j in range(1,r+1):
        r_f*=j
    for k in range(1,a+1):
        a_f*=k
    ans=n_f//a_f
    return ans
res=per(n,r,a)
print(res)
#perm---------------------- 7A
n=int(input("enter the number:"))
r=int(input("enter the number:"))
a=n-r
n_f=1
r_f=1
a_f=1
for i in range(1,n+1):
        n_f*=i
for j in range(1,r+1):
        r_f*=j
for k in range(1,a+1):
    a_f*=k
ans=n_f//a_f
print(ans)'''
#fac-------------------- 8
'''n=input()
temp=1
for i in range(1,int(n)+1):
    temp*=i
print(temp)
#fac---(------------- 8A
def fac(n):
    temp=1
    for i in range(1,int(n)+1):
        temp*=i
    return temp
n=input()
res=fac(n)
print(res)'''
#0,1,1,2,3,5,8 fibbi ----------- 9
'''n=int(input("enter the number of times:"))
a,b=0,1
print(a)
print(b)
for i in range(2,n+1):
    c=a+b
    print(c)
    a=b
    b=c
'''#fibbi------------------ 9A
'''def fib(a,b,n):
    print(a)
    print(b)
    for i in range(2,n):
        c=a+b
        print(c)
        a=b
        b=c
n=int(input("enter the number of times:"))
a=0
b=1
res=fib(a,b,n)'''
#prime----------------- 10
'''n=int(input("enter the number:"))
if n==1:
    print("neither composite nor prime")
elif n>1:
    for i in range(2,n):
        if (n%i==0):
            print("not a prime")
            break
    else:
        print("prime")'''
#prime ----------------- 10A
'''def pri(n):
        if (n==1):
            print("neither prime nor composite")
        elif n>1:
            for i in range(2,n):
                if(n%i==0):
                    print("not a prime")
                    break
            else:
                print("prime")
while True:
    u=input("enter the number to check:")

    if not (u.isdigit()) or (u==""):
         print("sorry")
         break
    else:
         n=int(u)
         res=pri(n)'''
# runrate ---------------------- 11
'''def run(o):
    temp=0
    for i in range(1,o+1):
        runs=int(input("enter the runs scored:"))
        a=temp+runs
        temp=a
        rr=(a/i)*o/overs
        pj=(a/i)*o
        print(f"runs scored {temp}   balls= {i}\n run rate is = {rr}  , projected score is {pj}")
        if i%6==0:
            ch=input("enter to continue(y/n)").lower()
            if ch!='y':
                break
team=input("enter the team name:")
overs=int(input("enter the overs:"))
o=overs*6
res=run(o)'''
#petrol----------------------------------- 12
'''t_lit=5000
t_price=102.1
a=int(input("enter the amount for purchase petrol:"))
lit=a/t_price
print("the litre you purchased is=",format(lit,"0.2f"))
l=int(input("enter the litre/litres:"))
amo=l*t_price
print("the amount is ",format(amo,"0.2f"))'''
#petrol --------------------------------- 12A
'''t_lit=5000
t_price=102.5

def amo(a):
    global t_lit
    lit=a/t_price
    li=format(lit,"0.2f")
    print(f"the amount you entered is {a}, for that you purchased petrol {li} litres.")
    t_lit-=lit
    print("the remaining litres in bluck is ",format(t_lit,"0.2f"))
    
def liti(l):
    global t_lit
    amo=l*t_price
    am=format(amo,"0.2f")
    print(f"the litres you entered is {l}, for that your amonut price is {am}.")
    t_lit-=l
    print("the remaining litres in bluck is ",format(t_lit,"0.2f"))


print("1-enter the amount:\n 2-enter the litres:\n 3-exit")
while True:
    ch=int(input("enter the choice above:"))
    if ch==1:
        a=int(input("enter the amount:"))
        res=amo(a)
    elif ch==2:
        l=int(input("enter the litres:"))
        res=liti(l)
    elif ch==3:
        exit()'''

