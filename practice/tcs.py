#choco_sum -------------------- 1 
'''import array as ar
n=int(input("enter the size of the array:"))
ch1=[int(input("enter the numbers:")) for _ in range(n)]
ch=ar.array('i',ch1)
fin=[]
if len(ch)!=n:
    print(f"the array size is {n} , you entered {len(ch)}")
else:
    for i in range(0,len(ch)):
        if ch[i]!=0:
            fin.append(ch[i])
    for i in range(0,len(ch)):
        if ch[i]==0:
            fin.append(ch[i])
print(*fin)'''


#def_choco  ---------------------- 1A
'''
import array as ar
def choco(n,ch):
    if len(ch)!=n:
        print(f"the size of array is {n},you entered {len(ch)}")
        return []
    else:
        fin=[]
        for i in range(0,len(ch)):
            if ch[i]!=0:
                fin.append(ch[i])
        for i in range(0,len(ch)):
            if ch[i]==0:
                fin.append(ch[i])
    return fin
n=int(input("enter the size of array:"))
ch1=[int(input("enter the numbers:")) for _ in range(n)]
ch=ar.array('i',ch1)   
ans=choco(n,ch)
print(*ans)'''

#bin --------------------------------- 2
'''n=int(input("enter the value:"))
a=n.bit_length()
m=(1<<a)-1
ans=n^m
print(ans)'''
#bin -----------------2A
'''def bin(n):
    a=n.bit_length()
    m=(1<<a)-1
    ans=n^m
    return ans
n=int(input("enter the number:"))
res=bin(n)
print(res)'''

#sunday------------------------------- 3
'''s_day=input("enter the starting day of month:").lower()
bet_days=int(input("enter the days to check:"))

days=["sun","mon","tue","wed","thu","fri","sat"]
s_day_index=days.index(s_day.lower())
con_sun=0

for i in range(bet_days):
    cur=days[(s_day_index + i) % 7]
    if cur=='sun':
        con_sun+=1
print("total sundays =",con_sun)'''
#sun---------------3A
'''def sun(n,s_day):
    days=["sun","mon","tue","wed","thu","fri","sat"]
    s_day_index=days.index(s_day.lower())
    tot_sun=0
    for i in range(n):
        cur=days[(s_day_index+i)%7]
        if cur=='sun':
            tot_sun+=1
    return tot_sun
n=int(input("enter the between days to check:"))
s_day=input("enter the day the month start:").lower()
res=sun(n,s_day)
print(res)
'''
#air------------------------4
'''import array as ar
n=int(input("enter the size of array:"))
arr1=[int(input("enter the number")) for i in range(n)] #to print new line 
#arr1=map(int,input("enter").split(","))----->single line
a=ar.array('i',arr1)

for i in range(0,len(a)-1):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print(*a)'''
#air---------------------------4A
'''import array as ar
def arra(a):
    for i in range(0,len(a)-1):
        for j in range(i+1,len(a)):
            if a[i]>a[j]:
                temp=a[i]
                a[i]=a[j]
                a[j]=temp
    return a
n=int(input("enter the size of array:"))
arr1=[int(input("enter the number")) for i in range(n)] #to print new line 
#arr1=map(int,input("enter").split(","))----->single line
a=ar.array('i',arr1)
res=arra(a)
print(*res)'''
#array----------------------5
'''import array as ar

n=int(input("size of array:"))
if  not (1<=n<=20):
    print(f"size is maximun,sorry....")
    exit()
arr1=[]
for i in range(n):
    num=int(input("enter the number:"))
    if not(1<=num<=10000):
        print(f"values are maximum")
        exit()
    arr1.append(num)
#arr1=[int(input("enter the number")) for i in range(n)]
arr=ar.array('i',arr1)
fin=[]
if len(arr)!=n:
    print(f"array size is {n},you entered {len(arr)} values")
else:
    fin.append(arr[0])
    a=arr[0]
    for i in range(1,len(arr)):
        if 1<=arr[i]<=10000:
            if arr[i]>a:
                fin.append(arr[i])
                a=arr[i]
    print(len(fin))'''
# array-----------------------------5A
'''import array as ar
import sys
def arri(n,arr1):
    if not (1 <= n<= 20):
        print(f"you entered {n} ,that is maximun , sorry......")
        sys.exit()
    arr=[]
    for k in range(0,len(arr1)):
        if not (1 <= arr1[k] <= 10000):
            print(f"you entered values are {arr} maximum,sorry.....")
            sys.exit()
        arr.append(arr1[k])
    fin=[]
    fin.append(arr[0])
    a=arr[0]
    for i in range(1,len(arr)):
        if arr[i]>a:
            fin.append(arr[i])
            a=arr[i]
    return len(fin)
n=int(input("enter the size of array:"))
arr2=[int(input("enter the number")) for i in range(n)]
arr1=ar.array('i',arr2)
res=arri(n,arr1)
print(res)
 '''
#pro------------------- 6
'''n=input("enter the number:")
temp=1
#for i in n:
#   a=int(i)
for i in range(0,len(n)):
    a=int(n[i])
    temp*=a
print(temp) '''   
#pro---------------------6A
'''def pro(n):
    temp=1
    for i in n:
        a=int(i)
        temp*=a
    return temp
n=input("enter the number:")
res=pro(n)
print(res)'''       
#furn------------------- 7
'''s=int(input("enter the size of the package:"))
if not(1 <= s <= 10):
    exit()  
colour=input("enter the colour available (a-aqua/b-black):") 
if not ( 1<= len(colour) <= 50):
    exit()
max_a=0
max_group=''
max_group_index=0
g_index=1
for i in range(0,len(colour),s):
    c=colour[i:i+s]
    d=c.count('a')
    if max_a<d:
        max_a=d
        max_group=c
        max_group_index=g_index
    g_index+=1
print(max_a)
print(max_group)
print(max_group_index)'''
#furn---------------------------- 7A
'''s=int(input("enter the group std to seperate:"))
if not (1 <= s <= 20):
    exit()
colour=input("enter the colours avaiable(a-aqua/b-black):")
if not (1 <= len(colour) <= 50):
    exit()
def furn(s,colour):
    max_a=0
    max_group=''
    max_group_index=0
    g_index=1
    for i in range(0,len(colour),s):
        c=colour[i:i+s]
        co=c.count('a')
        if max_a < co:
            max_a=co
            max_group=c
            max_group_index=g_index
        g_index+=1
    print(f"the number a maximun is{max_a}")
    print(f"the maximun a group is {max_group}")
    print(f"the maximun a group index is {max_group_index}")
res=furn(s,colour)
'''
#persi---------------8
'''n=int(input("enter the number of presidents :"))
if not (2 <= n <= 50):
    exit()
a=n-1
temp=1
for i in range(1,a+1):
    temp*=i
ans=2*temp
print(ans)'''
#persi-----------------8A
'''n=int(input("enter the number of presidents avaiable:"))
if not (2 <= n <= 50):
    exit()
a=n-1
def per(a):
    temp=1
    for i in range(1,a+1):
        temp*=i
    ans=2*temp
    return ans
res=per(a)
print(res)
'''
#threats---------------  9
'''n=int(input("enter the number:"))
if not (0 < n <= 10000):
    exit()
r=int(input("enter the repeating value:"))
if not (0 <= r <= 50):
    exit()
na=0
for i in str(n):
    a=int(i)
    na+=a
na1=na*r
na2=0
for i in str(na1):
    b=int(i)
    na2+=b
while na2>=10:
    na3=0
    for i in str(na2):
        c=int(i)
        na3+=c
    na2=na3
print(na2)'''
#therats---------------- 9a
'''n=int(input("enter the number :"))
if not (1 <= n <= 10000):
    exit()
r=int(input("enter the value:"))
if r==0:
    print('0')
    exit()
if not(1 <= r <= 50):
    exit()

def the(n,r):
    n1=0
    for i in str(n):
        a=int(i)
        n1+=a
    n2=n1*r
    n3=0
    for i in str(n2):
        b=int(i)
        n3+=b
    while n3>=10:
        n4=0
        for i in str(n3):
            c=int(i)
            n4+=c
        n3=n4
    return n3
res=the(n,r)
print(res)'''
#fine------------------ 10
'''n=int(input("enter the number of vehicles:"))
if not (0 < n <= 100):
    exit()
vh=[int(input("enter the vh number:")) for i in range(n)]
for k in range(0,len(vh)):
    if not (1<= vh[k] <= 9):
        exit()
date=int(input("enter the date:"))
if not(1 <= date <= 30):
    exit()
x=int(input("enter the fine of today:"))
if x == 0:
    print("0")
    exit()
if not (100 <= x <= 5000):
    exit()
fin=[]
if (date % 2)==0:
    for i in range(0,len(vh)):
        if vh[i]%2!=0:
            fin.append(vh[i])
    ans=len(fin)*x
    print(ans)
if (date % 2 )!=0:
    for j in range(0,len(vh)):
        if vh[j]%2==0:
            fin.append(vh[j])
    ans=len(fin)*x
    print(ans)
'''
#fine----------------- 10 A
'''n=int(input("enter the number of vehicles:"))
if not (1<=n<= 100):
    exit()
vh=[int(input("enter the vehicle number:")) for i in range(n)]
#ch=list(map(int,input("enter the vh(by comma)").split(",")))
for k in range(0,len(vh)):
    if not (1<=vh[k]<=9):
        exit()
d=int(input("enter the date;"))
if not (1<=d<=30):
    exit()
x=int(input("enter the fine amonut:"))
if (x==0):
    print("0")
    exit()
if not (100<=x<=5000):
    exit()
def fine(vh,d,x):
    fin=[]
    if (d%2==0):
        for i in range(0,len(vh)):
            if (vh[i]%2!=0):
                fin.append(vh[i])
    if (d%2!=0):
        for j in range(0,len(vh)):
            if (vh[j]%2==0):
                fin.append(vh[j])
    ans=len(fin)*x
    return ans
res=fine(vh,d,x)
print(res)'''

# tcs---> coding 10 ------------------------------------------------>> finish
# tcs---> advance section---->coding ------------------------------->>
# tcs----> placements paper----->advance coding -------------------->>
# tcs----> advance section---->advance coding ---------------------->>
# tcs---->advance section --->extra advanve coding ----------------->>








        
    
    
    
    


    
        


