import array as ar
num=int(input("enter the size of array:"))
n1=list(int(input("enter the number:")) for _ in range(num))
n=ar.array('i',n1)
print("you enter array is",n)
n3=[]
n2=ar.array('i',n3)
h=int(input("enter how many elements want to rotate:"))
side=input("enter left-l or right-r").lower()
if side=="l":
    for i in range(h,len(n)):
        n3.append(n[i])
    for i in range(0,h):
        n3.append(n[i])
    print(f"left rotation happen for {h} times and updated array is {n3}")
elif side=="r":
    for j in range(len(n)-h,len(n)):
        n3.append(n[j])
    for j in range(0,len(n)-h):
        n3.append(n[j])
    print(f"right rotation happen for {h} times and updated array is {n3}")
else:
    exit()

          
    
