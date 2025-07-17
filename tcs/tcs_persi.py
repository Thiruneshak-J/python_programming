'''n=int(input("enter the number of presidents:"))
pos=2
pos1=n-1
pos1_f=1
for i in range(1,pos1+1):
    pos1_f*=i
ans=pos*pos1_f
print(ans)
'''
def persident(n):
    pos=2
    pos1=n-1
    p_f=1
    for i in range(1,pos1+1):
        p_f*=i
    ans=pos*p_f
    return ans
n=int(input("enter the avaibable president:"))
if 2<=n and n<=50:
    res=persident(n)
    print("the possibilities are",res)
else:
    print("enter the correct avaibility")