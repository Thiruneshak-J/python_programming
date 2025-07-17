def ther(n,r):
    sum_of_n=0
    for i in str(n):
        a=int(i)
        sum_of_n+=a
    pos=sum_of_n*r
    sum_of_ans=0
    for i in str(pos):
        a=int(i)
        sum_of_ans+=a
    while sum_of_ans>=10:
        sums=0
        for i in str(sum_of_ans):
            a=int(i)
            sums+=a
        sum_of_ans=sums
    return sum_of_ans

n=int(input("enter the number of threats:"))
r=int(input("enter the number of times:"))

if 0<n<=1000 and 0<=r<=50:
    if r==0:
        print("0")
    else:
        res=ther(n,r)
        print(f"the answer is {res}")
    





