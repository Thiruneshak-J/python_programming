'''for i in range(0,5):
    for j in range(0,5):
        print("*",end="")
    print()
"*****"
"   *****"
"   *****"
"   *****"
"   *****"'''
'''for i in range(5,0,-1):
    for j in range(i):
        print("*",end="")
    print()
*****
****
***
**
*'''
'''for i in range(1,5):
    for j in range(i):
        print("*",end="")
    print()
*
**
***
****'''
'''for i in range(1,5):
    for j in range(i):
        print(i,end="")
    print()
1
22
333
4444'''
'''for i in range(1,5):
    for j in range(i):
        print(j+1,end="")
    print()
1
12
123
1234'''
'''for i in range(1,5):
    for j in range(i,0,-1):
        print(j,end="")
    print()
1
21
321
4321'''
'''for i in range(1,5):
    for j in range(i):
        print(chr(65+j),end='')
    print()
#chr(65+j)-----> start A,B,C........
#chr(97+j)-----> start a,b,c........'''
'''for i in range(1,6):
    for j in range(1,i+1):
        print(chr(64+j)*i,end="\t")
    print()
a
aa bb
aaa bbb ccc
aaaa bbbb cccc dddd
aaaaa bbbbb ccccc ddddd eeeee'''
'''r=5
for i in range(5):
    for j in range(i,0,-1):
        print("",end="")
    for k in range(2*i)
    print()'''

'''n=list(map(str,input("enter the word:")))
for i in range(len(n),0,-1):
    for j in range(i):
        print(n[j],end="")
    print()'''
'''r=5
for i in range(r):
    for j in range(r-i+1):
        print(" ",end="")
    for k in range(2*i+1):
        if k==0 or k==2*i or i==r-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()'''
'''r=5
for i in range(r):
    for j in range(i):
        print(" ",end="")
    for k in range(r-i+4):
        if k==0 or k==8-2*i or i==0:
            print("*",end="")
        else:
            print(" ",end="")
    print()
'''
'''n=5
for i in range(n):
    for j in range(n):
        if i==0 or i==4 or j==0:
            print("*",end="")
    print()'''
'''n=5
for i in range(n):
    for j in range(9):
        if j==0 or j==2*i or i==4:
            print("*",end="")
        else:
            print(" ",end="")
    print()'''
n=5
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for k in range(2*i+1):
        print("*",end="")
    print()
for i in range(n):
    for j in range(i):
        print(" ",end="")
    for k in range(9-2*i):
        print("*",end="")
    print()
'''n=5
for i in range(n):
    for j in range(i):
        print(" ",end="")
    for k in range(n-i):
        if k==0 or k==n-i -1 or i==0:
            print("*",end="")
        else:
            print(" ",end="")
    print()
'''
