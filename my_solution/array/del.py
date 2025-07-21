import array as ar
num=int(input("enter the size of array:"))
n1=[int(input("enter the number:")) for _ in range(num)]
n=ar.array('i',n1)
print("you entered array is :",n)
while True:
    pos=int(input("enter the index of array to remove:"))
    for i in range(0,len(n)):
        if i==pos:
            n.remove(n[i])
    print(n)
    ch=input("enter y/n:").lower()
    if ch!='y':
        break
