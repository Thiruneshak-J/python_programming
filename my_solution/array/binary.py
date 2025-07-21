import array as ar
n1=list(map(int,input("enter the number:").split(" ")))
n=ar.array('i',n1)
print("you enter numbers are :",n)
e=int(input("enter the number to find:"))
l=int()
m=int()
h=int(len(n)-1)
while(l<=h):
    m=(l+h)//2
    if n[m]==e:
        print("the element is in index :",m)
        print("the element is in position :",m+1)
        break
    elif n[m]<e:
        l=m+1
    else:
        h=m-1
    




























































































































































