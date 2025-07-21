'''def fib(n):
    li=[]
    a=0
    b=1
    li.append(b)
    for i in range(2,n+1):
        c=a+b
        li.append(c)
        a=b
        b=c
    return li
def prime(n):
    pi=[]
    i=2
    while len(pi)<n:
        f=True
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                f=False
                break
        if f:
            pi.append(i)
        i+=1
    return pi
def add(res,res1):
    a=res
    b=res1
    fin=[]
    #min_len=min(len(a),len(b))
    for i in range(len(a)):
        fin.append(a[i])
        fin.append(b[i])
    #fin.extend(a[min_len:])
    #fin.extend(b[min_len:])
    return fin
def fi(n,res2):
    return res2[n-1]
n=int(input("enter the number:"))
res=fib(n)
res1=prime(n)
res2=add(res,res1)
res3=fi(n,res2)
#print(res)
#print(res1)
#print(res2)
print(res3)'''
'''def fib(n):
    li=[]
    a=0
    b=1
    li.append(b)
    for i in range(2,n+1):
        c=a+b
        li.append(c)
        a=b
        b=c
    return li
def pri(n):
    pi=[]
    i=2
    while len(pi)<n:
        f=False
        for j in range(2,int(i**0.5)+1):
            if i % j==0:
                f=True
                break
        if f==False:
            pi.append(i)
        i+=1
    return pi
def get(res,res1):
    a=res
    b=res1
    fin=[]
    min_i=min(len(a),len(b))
    for i in range(min_i):
        fin.append(a[i])
        fin.append(b[i])
    fin.extend(a[min_i:])
    fin.extend(b[min_i:])
    return fin
def get2(n,res3):
    return res3[n-1]

n=int(input("enter the numebr:"))
res=fib(n)
res1=pri(n)
'''
def fib(n):
    li=[]
    a=0
    b=1
    li.append(b)
    for i in range(2,n+1):
        c=a+b
        li.append(c)
        a=b
        b=c
    return li
def pri(n):
    pi=[]
    i=2
    while len(pi)<n:
        f=False
        for j in range(2,int(i**0.5)+1):
            if (i%j==0):
                f=True
                break
        if f==False:
            pi.append(i)
        i+=1
    return pi
def get(n):
    fib_count=(n+1)//2
    pri_count=n//2

    fib_seq=fib(fib_count)
    pri_seq=pri(pri_count)

    if n % 2==1:
        return fib_seq[n//2]
    else:
        return pri_seq[(n//2)-1]
n=int(input("enter the number:"))
print(get(n))

                